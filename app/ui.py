import streamlit as st
import pandas as pd
import os

from monitor import get_system_metrics
from health import calculate_health_score, get_health_status
from process_monitor import get_top_processes
from alerts import generate_alerts
from process_alerts import generate_process_alerts
from ai_analyzer import analyze_system


# =========================
# PAGE CONFIGURATION
# =========================

st.set_page_config(
    page_title="System Health Monitor",
    page_icon="🖥️",
    layout="wide"
)


# =========================
# TITLE
# =========================

st.title("🖥️ Automated System Health Monitor")

st.caption(
    "Real-time system monitoring with AI-powered analysis and recommendations"
)


# =========================
# GET CURRENT SYSTEM DATA
# =========================

metrics = get_system_metrics()

health_score = calculate_health_score(metrics)

health_status = get_health_status(health_score)

processes = get_top_processes()

system_alerts = generate_alerts(metrics)

process_alerts = generate_process_alerts(processes)


# =========================
# SYSTEM METRICS
# =========================

st.subheader("📊 System Metrics")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "CPU Usage",
        f"{metrics['cpu']}%"
    )

with col2:
    st.metric(
        "Memory Usage",
        f"{metrics['memory']}%"
    )

with col3:
    st.metric(
        "Disk Usage",
        f"{metrics['disk']}%"
    )

with col4:
    st.metric(
        "Health Score",
        f"{health_score}/100"
    )


# =========================
# HEALTH STATUS
# =========================

st.subheader("🩺 System Health")

if health_status == "Healthy":

    st.success(
        f"System Status: {health_status}"
    )

elif health_status == "Warning":

    st.warning(
        f"System Status: {health_status}"
    )

else:

    st.error(
        f"System Status: {health_status}"
    )


# =========================
# PROCESS MONITORING
# =========================

st.subheader("🔥 Top Resource-Consuming Processes")

process_data = pd.DataFrame(processes)

if not process_data.empty:

    process_data = process_data.rename(
        columns={
            "pid": "PID",
            "name": "Process",
            "cpu": "CPU (%)",
            "memory": "Memory (%)"
        }
    )

    st.dataframe(
        process_data,
        use_container_width=True,
        hide_index=True
    )

else:

    st.info(
        "No process information available."
    )


# =========================
# SYSTEM ALERTS
# =========================

st.subheader("🚨 System Alerts")

if system_alerts:

    for alert in system_alerts:
        st.warning(alert)

else:

    st.success(
        "No system-level alerts."
    )


# =========================
# PROCESS ALERTS
# =========================

st.subheader("⚠️ Process Alerts")

if process_alerts:

    for alert in process_alerts:
        st.warning(alert)

else:

    st.success(
        "No process-level alerts."
    )


# =========================
# AI ANALYSIS
# =========================

st.subheader("🤖 AI System Analysis")

st.caption(
    "Run AI analysis only when you want an intelligent assessment "
    "of the current system condition."
)


if st.button("🔍 Run AI Analysis"):

    with st.spinner(
        "AI is analyzing the current system condition..."
    ):

        ai_analysis = analyze_system(
            metrics,
            system_alerts,
            processes
        )

    st.session_state["ai_analysis"] = ai_analysis


if "ai_analysis" in st.session_state:

    st.info(
        st.session_state["ai_analysis"]
    )

else:

    st.info(
        "Click 'Run AI Analysis' to generate an "
        "AI-powered system assessment."
    )


# =========================
# HISTORICAL DATA
# =========================

st.subheader("📈 Historical Metrics")

DATA_FILE = os.path.join(
    os.path.dirname(os.path.dirname(__file__)),
    "data",
    "metrics.csv"
)


if os.path.exists(DATA_FILE):

    history = pd.read_csv(DATA_FILE)

    if not history.empty:

        history["timestamp"] = pd.to_datetime(
            history["timestamp"]
        )

        st.line_chart(
            history.set_index("timestamp")[
                ["cpu", "memory", "disk"]
            ]
        )

    else:

        st.info(
            "Historical data is empty."
        )

else:

    st.info(
        "Historical metrics file not found."
    )


# =========================
# FOOTER
# =========================

st.divider()

st.caption(
    "Automated System Health Monitor • "
    "Python • Streamlit • psutil • Hugging Face AI"
)