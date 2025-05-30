from scapy.all import sniff, IP
from database import insert_traffic
from alerts import check_for_anomalies

def process_packet(packet):
    if packet.haslayer(IP):
        ip = packet[IP].src
        proto = packet[IP].proto
        insert_traffic(ip, str(proto), len(packet))
        check_for_anomalies(ip, str(proto))

def start_monitoring():
    import threading
    t = threading.Thread(target=lambda: sniff(prn=process_packet, store=0))
    t.daemon = True
    t.start()
