from scapy.all import rdpcap, TCP, IP
import pandas as pd
import matplotlib.pyplot as plt

packets = rdpcap("test-1.pcap")

outstanding = {}
rtt_list = []

for pkt in packets:
    if pkt.haslayer(IP) and pkt.haslayer(TCP):
        ip = pkt[IP]
        tcp = pkt[TCP]

        # Calculate payload length
        payload_len = len(tcp.payload)

        # Key: (src, dst, seq_end)
        seq_end = tcp.seq + payload_len
        key = (ip.src, ip.dst, seq_end)

        # Store the send time of this data packet
        if payload_len > 0:  
            outstanding[key] = pkt.time

        # If it's an ACK, check if it matches a sent packet
        elif tcp.flags == "A":  
            match = (ip.dst, ip.src, tcp.ack)
            if match in outstanding:
                rtt = pkt.time - outstanding[match]
                rtt_list.append(rtt)
                del outstanding[match]  # clean up

# Put into DataFrame
df = pd.DataFrame(rtt_list, columns=["RTT"])

print(df.head())

# Plot
plt.plot(df.index, df["RTT"], marker='o')
plt.title("TCP Data-ACK RTT Over Time")
plt.xlabel("Packet Index")
plt.ylabel("RTT (seconds)")
plt.show()
