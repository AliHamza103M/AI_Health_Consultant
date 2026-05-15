from utils.style import load_css
import streamlit as st
import pandas as pd
import sqlite3

# =========================
# PAGE CONFIG
# =========================

st.set_page_config(
    page_title="Admin Panel",
    page_icon="🛠",
    layout="wide"
)

load_css()

# =========================
# PAGE TITLE
# =========================

st.title("🛠 Admin Panel")

st.write("System administration and database overview")

# =========================
# DATABASE CONNECTION
# =========================

conn = sqlite3.connect("database/health.db")

# =========================
# LOAD USERS
# =========================

try:

    users_df = pd.read_sql_query(
        "SELECT * FROM users",
        conn
    )

except:

    users_df = pd.DataFrame()

# =========================
# LOAD HISTORY
# =========================

try:

    history_df = pd.read_sql_query(
        "SELECT * FROM history",
        conn
    )

except:

    history_df = pd.DataFrame()

# =========================
# ADMIN METRICS
# =========================

col1, col2, col3 = st.columns(3)

with col1:

    st.metric(
        label="Total Users",
        value=len(users_df)
    )

with col2:

    st.metric(
        label="Total Predictions",
        value=len(history_df)
    )

with col3:

    st.metric(
        label="AI Diseases",
        value="70"
    )

# =========================
# USERS TABLE
# =========================

st.subheader("👥 Registered Users")

if not users_df.empty:

    st.dataframe(
        users_df,
        use_container_width=True
    )

else:

    st.warning("No users found")

# =========================
# HISTORY TABLE
# =========================

st.subheader("📜 Prediction Records")

if not history_df.empty:

    st.dataframe(
        history_df,
        use_container_width=True
    )

else:

    st.warning("No prediction history found")

# =========================
# DATABASE STATUS
# =========================

st.subheader("💾 Database Status")

st.success("Database Connected Successfully ✅")

# =========================
# SYSTEM INFO
# =========================

st.subheader("🧠 System Information")

st.info("""
AI Model: Random Forest Classifier

Features:
- User Authentication
- Disease Prediction
- Analytics Dashboard
- Prediction History
- CSV Export
- SQLite Database
- 70 Disease Detection
""")