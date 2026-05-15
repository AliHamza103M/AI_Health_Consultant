from utils.style import load_css
import streamlit as st
import pandas as pd
import sqlite3

# =========================
# PAGE CONFIG
# =========================

st.set_page_config(
    page_title="Dashboard",
    page_icon="📊",
    layout="wide"
)
load_css()
# =========================
# PAGE TITLE
# =========================

st.title("📊 AI Health Consultant Dashboard")

st.write("Welcome to the AI-Powered Health Prediction System")

# =========================
# DATABASE CONNECTION
# =========================

conn = sqlite3.connect("database/health.db")

# =========================
# LOAD HISTORY DATA
# =========================

try:

    df = pd.read_sql_query("SELECT * FROM history", conn)

except:

    df = pd.DataFrame()

# =========================
# DASHBOARD METRICS
# =========================

col1, col2, col3 = st.columns(3)

with col1:

    st.metric(
        label="Total Predictions",
        value=len(df)
    )

with col2:

    st.metric(
        label="Total Diseases",
        value="70"
    )

with col3:

    st.metric(
        label="AI Model",
        value="Random Forest"
    )

# =========================
# SYSTEM INFORMATION
# =========================

st.subheader("🧠 System Information")

st.info("""
This AI system predicts diseases based on symptoms using Machine Learning.

Features:
- 70 Disease Detection
- AI-Based Prediction
- Symptom Analysis
- Prediction Confidence Score
- User Authentication
- Prediction History
""")

# =========================
# RECENT HISTORY
# =========================

st.subheader("📜 Recent Prediction History")

if not df.empty:

    st.dataframe(df.tail(10))

else:

    st.warning("No prediction history available")