#Network Dashboard é uma aplicação web que monitoriza o tráfego da rede local em tempo real

from flask import Flask, render_template, jsonify
from database import get_traffic_data, get_alerts
from monitor import start_monitoring

app = Flask(__name__)

@app.route('/')
def dashboard():
    return render_template('dashboard.html')

@app.route('/api/traffic')
def traffic():
    return jsonify(get_traffic_data())

@app.route('/api/alerts')
def alerts():
    return jsonify(get_alerts())

if __name__ == '__main__':
    start_monitoring()
    app.run(debug=True)
