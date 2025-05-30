import sqlite3

def init_db():
    conn = sqlite3.connect('network.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS traffic (
        timestamp TEXT, ip TEXT, protocol TEXT, bytes INT)''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS alerts (
        timestamp TEXT, alert TEXT)''')
    conn.commit()
    conn.close()

def insert_traffic(ip, protocol, bytes):
    conn = sqlite3.connect('network.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO traffic VALUES (datetime('now'), ?, ?, ?)", (ip, protocol, bytes))
    conn.commit()
    conn.close()

def insert_alert(alert):
    conn = sqlite3.connect('network.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO alerts VALUES (datetime('now'), ?)", (alert,))
    conn.commit()
    conn.close()

def get_traffic_data():
    conn = sqlite3.connect('network.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM traffic ORDER BY timestamp DESC LIMIT 100")
    rows = cursor.fetchall()
    conn.close()
    return [{"timestamp": r[0], "ip": r[1], "protocol": r[2], "bytes": r[3]} for r in rows]

def get_alerts():
    conn = sqlite3.connect('network.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM alerts ORDER BY timestamp DESC LIMIT 20")
    rows = cursor.fetchall()
    conn.close()
    return [{"timestamp": r[0], "alert": r[1]} for r in rows]
