from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

threats = [
    {"timestamp": "2025-02-12 14:00", "source_ip": "192.168.1.10", "threat": "Malware Detected"},
    {"timestamp": "2025-02-12 14:05", "source_ip": "192.168.1.15", "threat": "DDoS Attack"}
]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/traffic')
def traffic():
    return render_template('traffic.html', threats=threats)

@app.route('/alerts')
def alerts():
    return render_template('alerts.html', threats=threats)

@app.route('/api/threats', methods=['GET'])
def get_threats():
    return jsonify(threats)

if __name__ == '__main__':
    app.run(debug=True)


