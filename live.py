from scapy.all import sniff, TCP, IP
import time

rtt_list = []
outstanding = {}

def process_packet(pkt):
    global rtt_list
    if pkt.haslayer(IP) and pkt.haslayer(TCP):
        if pkt[TCP].flags == "S":  # SYN
            key = (pkt[IP].src, pkt[TCP].seq)
            outstanding[key] = pkt.time
        elif pkt[TCP].flags == "SA":  # SYN-ACK
            match = (pkt[IP].dst, pkt[TCP].ack - 1)
            if match in outstanding:
                rtt = pkt.time - outstanding[match]
                print(f"RTT: {rtt:.6f} seconds")
                rtt_list.append(rtt)

# sniff 100 packets on Wi-Fi (replace with "eth0" for Ethernet)
sniff(iface="Wi-Fi", prn=process_packet, count=100)
