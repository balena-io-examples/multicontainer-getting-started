import time
from flask import Flask, jsonify

app = Flask(__name__)


def _read_proc_cpu_totals():
    with open("/proc/stat", "r", encoding="utf-8") as proc_stat:
        cpu_line = proc_stat.readline().strip()

    parts = cpu_line.split()
    counters = [int(value) for value in parts[1:]]

    idle = counters[3]
    iowait = counters[4] if len(counters) > 4 else 0
    idle_all = idle + iowait
    total = sum(counters)
    return total, idle_all


def _cpu_percent_once(interval):
    previous_total, previous_idle = _read_proc_cpu_totals()
    time.sleep(interval)
    current_total, current_idle = _read_proc_cpu_totals()

    total_delta = current_total - previous_total
    idle_delta = current_idle - previous_idle

    if total_delta <= 0:
        return 0.0

    busy_delta = total_delta - idle_delta
    return (busy_delta / total_delta) * 100.0


def _cpu_percent(interval=0.5, samples=5):
    if samples <= 0:
        return 0.0

    sample_interval = interval / samples
    sample_values = [_cpu_percent_once(sample_interval) for _ in range(samples)]
    return sum(sample_values) / len(sample_values)


def _load_1m():
    with open("/proc/loadavg", "r", encoding="utf-8") as proc_loadavg:
        return float(proc_loadavg.readline().split()[0])


@app.get("/cpu")
def cpu_usage():
    usage_percent = _cpu_percent(interval=0.5, samples=5)
    one_minute_load = _load_1m()
    return jsonify({"cpu_percent": usage_percent, "load_1m": one_minute_load})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
