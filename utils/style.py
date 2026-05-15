import streamlit as st

def load_css():

    st.markdown("""
    <style>

    /* MAIN BACKGROUND */

    .stApp {
        background-color: #f4f7fc;
    }

    /* SIDEBAR */

    section[data-testid="stSidebar"] {
        background-color: #020c2b;
    }

    section[data-testid="stSidebar"] * {
        color: white;
    }

    /* HEADINGS */

    h1, h2, h3 {
        color: #111827;
        font-weight: 800;
    }

    /* BUTTONS */

    button[kind="primary"] {
        background-color: #2563eb !important;
        color: white !important;
        border-radius: 10px !important;
        border: none !important;
        height: 50px !important;
        font-size: 18px !important;
        font-weight: bold !important;
    }

    button[kind="primary"]:hover {
        background-color: #1d4ed8 !important;
        color: white !important;
    }

    /* NORMAL BUTTONS */

    .stButton button {
        background-color: #2563eb !important;
        color: white !important;
        border-radius: 10px !important;
        border: none !important;
        padding: 10px 20px !important;
        font-weight: bold !important;
    }

    .stButton button:hover {
        background-color: #1d4ed8 !important;
        color: white !important;
    }

    /* CARDS */

    div[data-testid="metric-container"] {
        background-color: white;
        border-radius: 12px;
        padding: 15px;
        box-shadow: 0px 2px 12px rgba(0,0,0,0.1);
    }

    /* TABLE */

    .stDataFrame {
        background-color: white;
        border-radius: 12px;
        padding: 10px;
    }

    </style>
    """, unsafe_allow_html=True)