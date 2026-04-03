import os
from flask import Flask, jsonify
import psutil

app = Flask(__name__)


@app.get("/cpu")
def cpu_usage():
    # Percentage of CPU usage across all cores.
    usage_percent = psutil.cpu_percent(interval=0.1)
    one_minute_load = os.getloadavg()[0]
    return jsonify({"cpu_percent": usage_percent, "load_1m": one_minute_load})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
