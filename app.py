"""
MediPi Hackathon - Starter Flask App
Run with: python3 app.py
Access from any device on same network at: http://<pi-ip>:5000
"""

from flask import Flask, jsonify, render_template
import time
import threading

from sensors.mock_sensor import read_sensor_data  # swap this for real sensor once known

app = Flask(__name__)

# Shared state - latest reading, updated by background thread
latest_data = {
    "value": None,
    "status": "starting",
    "timestamp": None
}


def sensor_loop():
    """Continuously reads sensor in the background so the web page is never blocked."""
    while True:
        try:
            reading = read_sensor_data()
            latest_data["value"] = reading
            latest_data["status"] = "ok"
            latest_data["timestamp"] = time.strftime("%H:%M:%S")
        except Exception as e:
            latest_data["status"] = f"error: {e}"
        time.sleep(1)  # adjust polling rate as needed


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/api/data")
def api_data():
    """Frontend polls this endpoint to get live sensor readings as JSON."""
    return jsonify(latest_data)


@app.route("/health")
def health():
    return jsonify({"status": "Pi is alive"})


if __name__ == "__main__":
    # start background sensor thread
    t = threading.Thread(target=sensor_loop, daemon=True)
    t.start()

    # host="0.0.0.0" makes it reachable from your phone/laptop, not just the Pi itself
    app.run(host="0.0.0.0", port=5000, debug=True)
