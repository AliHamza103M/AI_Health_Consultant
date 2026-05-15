import streamlit as st
import sqlite3
import pandas as pd
import plotly.express as px

from utils.style import load_css

# =========================
# PAGE CONFIG
# =========================

st.set_page_config(
    page_title="Analytics",
    page_icon="📊",
    layout="wide"
)

load_css()

# =========================
# TITLE
# =========================

st.title("📊 Disease Prediction Analytics")

st.write("Analytics and insights from prediction history.")

# =========================
# DATABASE CONNECTION
# =========================

conn = sqlite3.connect("database/health.db")

# =========================
# LOAD HISTORY
# =========================

query = """
SELECT *
FROM history
"""

df = pd.read_sql_query(query, conn)

# =========================
# CHECK DATA
# =========================

if len(df) == 0:

    st.warning("No analytics data available.")

else:

    # =========================
    # TOTAL PREDICTIONS
    # =========================

    total_predictions = len(df)

    # =========================
    # MOST COMMON DISEASE
    # =========================

    most_common = df["disease"].value_counts().idxmax()

    # =========================
    # AVERAGE CONFIDENCE
    # =========================

    avg_confidence = df["confidence"].mean()

    # =========================
    # TOP CARDS
    # =========================

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Total Predictions",
            total_predictions
        )

    with col2:
        st.metric(
            "Most Common Disease",
            most_common
        )

    with col3:
        st.metric(
            "Average Confidence",
            f"{avg_confidence:.2f}%"
        )

    st.divider()

    # =========================
    # DISEASE COUNT
    # =========================

    disease_counts = (
        df["disease"]
        .value_counts()
        .reset_index()
    )

    disease_counts.columns = [
        "Disease",
        "Count"
    ]

    # =========================
    # BAR CHART
    # =========================

    st.subheader("📈 Disease Frequency")

    fig_bar = px.bar(
        disease_counts,
        x="Disease",
        y="Count",
        color="Count",
        title="Disease Prediction Frequency"
    )

    st.plotly_chart(
        fig_bar,
        use_container_width=True
    )

    # =========================
    # PIE CHART
    # =========================

    st.subheader("🥧 Disease Distribution")

    fig_pie = px.pie(
        disease_counts,
        names="Disease",
        values="Count",
        title="Disease Distribution"
    )

    st.plotly_chart(
        fig_pie,
        use_container_width=True
    )

    # =========================
    # TABLE
    # =========================

    st.subheader("📋 Prediction Records")

    st.dataframe(
        df,
        use_container_width=True
    )