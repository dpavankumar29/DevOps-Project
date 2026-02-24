from flask import Flask
from prometheus_client import start_http_server, Counter
import time
import random

app = Flask(__name__)

REQUEST_COUNT = Counter('request_count', 'Total Request Count')

@app.route("/")
def home():
    REQUEST_COUNT.inc()
    return "DevOps Monitoring App is Running!"

@app.route("/health")
def health():
    return {"status": "healthy"}

if __name__ == "__main__":
    start_http_server(8001)  # Prometheus metrics port (internal)
    app.run(host="0.0.0.0", port=5055)