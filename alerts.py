from database import insert_alert
from collections import defaultdict
import time

ip_counter = defaultdict(list)

def check_for_anomalies(ip, proto):
    now = time.time()
    ip_counter[ip].append(now)
    ip_counter[ip] = [t for t in ip_counter[ip] if now - t < 10]

    if len(ip_counter[ip]) > 50:
        insert_alert(f"Possible flood attack from {ip}")
