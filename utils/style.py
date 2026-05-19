import streamlit as st
import base64

# =========================
# IMAGE FUNCTION
# =========================

def get_base64(file_path):

    with open(file_path, "rb") as f:

        data = f.read()

    return base64.b64encode(data).decode()

# =========================
# LOAD CSS
# =========================

def load_css():

    bg_image = get_base64("assets/bg.png")

    st.markdown(f"""
    <style>

    /* =========================
       MAIN BACKGROUND
    ========================= */

    .stApp {{
        background-image: url("data:image/png;base64,{bg_image}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}

    /* =========================
       HIDE OLD STREAMLIT MENU
    ========================= */

    section[data-testid="stSidebarNav"] > ul {{
        display: none;
    }}

    /* =========================
       SIDEBAR
    ========================= */

    section[data-testid="stSidebar"] {{
        background: rgba(0, 15, 45, 0.95);
        border-right: 2px solid #2563eb;
    }}

    /* =========================
       SIDEBAR TEXT
    ========================= */

    section[data-testid="stSidebar"] * {{
        color: white !important;
        font-size: 21px !important;
        font-weight: bold !important;
    }}

    /* =========================
       CUSTOM BUTTONS
    ========================= */

    div[data-testid="stSidebarNav"] a {{
        background-color: rgba(255,255,255,0.08);
        border-radius: 14px;
        margin-bottom: 10px;
        padding: 12px;
        transition: 0.3s;
    }}

    div[data-testid="stSidebarNav"] a:hover {{
        background: #2563eb;
        transform: scale(1.02);
    }}

    /* =========================
       MAIN TEXT
    ========================= */

    h1,h2,h3,h4,h5,h6,p,li {{
        color: white !important;
    }}

    </style>
    """, unsafe_allow_html=True)