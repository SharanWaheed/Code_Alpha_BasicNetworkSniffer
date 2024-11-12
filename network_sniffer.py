from scapy.all import sniff

# Define a callback function to process each packet
def packet_callback(packet):
    print(packet.summary())  # Print a summary of each packet
    if packet.haslayer("IP"):  # Check if the packet contains an IP layer
        print("Source IP:", packet["IP"].src)
        print("Destination IP:", packet["IP"].dst)
        print("Protocol:", packet["IP"].proto)
        print("-" * 50)

# Start sniffing (requires root privileges)
print("Starting packet capture...")
sniff(filter="ip", prn=packet_callback, count=10)  # Capture 10 IP packets
