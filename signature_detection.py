from scapy.layers.inet import IP

# List of known malicious IP addresses
MALICIOUS_IPS = {"192.168.1.100", "10.0.0.5"}

def detect_signature(packet):
    if packet.haslayer(IP):  # Corrected variable name
        src_ip = packet[IP].src  # Fixed assignment
        if src_ip in MALICIOUS_IPS:  # Fixed condition
            print(f"[ALERT] Malicious IP detected: {src_ip}")
