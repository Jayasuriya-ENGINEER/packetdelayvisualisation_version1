from scapy.all import rdpcap, TCP, IP
import matplotlib.pyplot as plt
import pandas as pd

packets = rdpcap("sample_pack.pcap")

data = []
for pkt in packets:
    if pkt.haslayer(TCP):
        time = pkt.time  # timestamp
        src = pkt[0][1].src
        dst = pkt[0][1].dst
        seq = pkt[TCP].seq
        ack = pkt[TCP].ack
        data.append([time, src, dst, seq, ack])

df = pd.DataFrame(data, columns=["time", "src", "dst", "seq", "ack"])
print(df.head())

rtt_list = []
outstanding = {}

for pkt in packets:
    if pkt.haslayer(TCP):
        key = (pkt[IP].src, pkt[TCP].seq)  # identify packet by src+seq
        if pkt[TCP].flags == "S":  # SYN packet
            outstanding[key] = pkt.time
        elif pkt[TCP].flags == "SA":  # SYN-ACK response
            # Match reply to SYN
            match = (pkt[IP].dst, pkt[TCP].ack - 1)
            if match in outstanding:
                rtt = pkt.time - outstanding[match]
                rtt_list.append(rtt)

print("TCP RTT values:", rtt_list)

plt.plot(rtt_list, marker='o')
plt.title("RTT Over Time")
plt.xlabel("Packet Index")
plt.ylabel("RTT (seconds)")
plt.show()

