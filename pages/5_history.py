import streamlit as st
import sqlite3
import pandas as pd

from utils.style import load_css

# =========================
# PAGE CONFIG
# =========================

st.set_page_config(
    page_title="Prediction History",
    page_icon="📜",
    layout="wide"
)

load_css()

# =========================
# TITLE
# =========================

st.title("📜 Prediction History")

st.write("View all previous disease predictions.")

# =========================
# DATABASE CONNECTION
# =========================

conn = sqlite3.connect("database/health.db")

# =========================
# LOAD DATA
# =========================

query = """
SELECT
    id,
    username,
    disease,
    confidence,
    symptoms
FROM history
ORDER BY id DESC
"""

df = pd.read_sql_query(query, conn)

# =========================
# SEARCH SECTION
# =========================

st.subheader("🔍 Search Filters")

col1, col2 = st.columns(2)

with col1:

    username_search = st.text_input(
        "Search by Username"
    )

with col2:

    disease_search = st.text_input(
        "Search by Disease"
    )

# =========================
# FILTER DATA
# =========================

filtered_df = df.copy()

# USERNAME FILTER

if username_search:

    filtered_df = filtered_df[
        filtered_df["username"]
        .str.contains(
            username_search,
            case=False
        )
    ]

# DISEASE FILTER

if disease_search:

    filtered_df = filtered_df[
        filtered_df["disease"]
        .str.contains(
            disease_search,
            case=False
        )
    ]

# =========================
# SHOW RESULTS
# =========================

st.subheader("📋 Prediction Records")

if len(filtered_df) > 0:

    st.dataframe(
        filtered_df,
        use_container_width=True
    )

else:

    st.warning("No matching records found.")