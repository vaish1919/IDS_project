import pandas as pd
import numpy as np
from scapy.layers.inet import IP, TCP, UDP

def extract_features(packet):
    if packet.haslayer(IP):
        return [
            len(packet),
            packet[IP].ttl,
            1 if packet.haslayer(TCP) else 0,
            1 if packet.haslayer(UDP) else 0,
        ]
    return None