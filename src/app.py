from flask import Flask, jsonify
import socket
from datetime import datetime

app = Flask(__name__)

def get_hostname():
    return socket.gethostname()

def get_date_dd_mm_yyyy():
    return datetime.now().strftime("%d-%m-%Y")

@app.route('/api/v1/details')
def details():
    return "Hello World"

@app.route('/api/v1/healthz')
def healthz():
    return jsonify(status="up")

@app.route('/api/v1/hostname')
def hostname():
    return jsonify(hostname=get_hostname())

@app.route('/api/v1/date')
def date():
    return jsonify(date=get_date_dd_mm_yyyy())

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
