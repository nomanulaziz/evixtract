from scapy.all import sniff, IP
from scapy.utils import wrpcap

def capture_packets(filter_rule=None, packet_count=100):
    print(f"Capturing {packet_count} packets...")
    packets = sniff(filter=filter_rule, count=packet_count)
    return packets  

def analyze_packets(packets):
    for packet in packets:
        if IP in packet:
            if packet[IP].dst == "192.168.141.131":  
                print(f"Suspicious packet from {packet[IP].src} to {packet[IP].dst}")

def save_packets_to_file(packets, filename="capture.pcap"):
    wrpcap(filename, packets)
    print(f"Packets saved to {filename}")
