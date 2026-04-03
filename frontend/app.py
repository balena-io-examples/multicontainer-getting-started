import time

import pandas as pd
import requests
import streamlit as st

st.set_page_config(page_title="CPU Usage", page_icon="CPU", layout="wide")
st.title("CPU Usage")

history = st.session_state.setdefault("cpu_percent_history", [])
load_history = st.session_state.setdefault("load_1m_history", [])

if st.button("Refresh"):
    pass

try:
    response = requests.get("http://data:8080/cpu", timeout=2)
    response.raise_for_status()
    payload = response.json()
    cpu_value = payload.get("cpu_percent")
    load_value = payload.get("load_1m")
    if cpu_value is not None:
        history.append(float(cpu_value))
        if len(history) > 120:
            del history[:-120]
    if load_value is not None:
        load_history.append(float(load_value))
        if len(load_history) > 120:
            del load_history[:-120]
except requests.RequestException as exc:
    st.error(f"Could not reach data service: {exc}")

if history:
    st.metric("CPU usage", f"{history[-1]:.1f}%")
    chart_data = pd.DataFrame(
        {
            "sample": list(range(1, len(history) + 1)),
            "cpu_percent": history,
        }
    ).set_index("sample")
    st.line_chart(chart_data, use_container_width=True)
    if load_history:
        st.caption(f"1-minute load average: {load_history[-1]:.2f}")
else:
    st.info("No CPU data yet.")

# Keep the UI simple and alive without client-side JS.
time.sleep(2)
st.rerun()
