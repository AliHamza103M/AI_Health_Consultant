import streamlit as st

from utils.cards import show_cards
from utils.database import create_tables
from utils.style import load_css

# =========================
# PAGE CONFIG
# =========================

st.set_page_config(
    page_title="AI Health Consultant",
    page_icon="🩺",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================
# LOAD CSS
# =========================

load_css()

# =========================
# DATABASE
# =========================

create_tables()

# =========================
# HIDE DEFAULT STREAMLIT UI
# =========================

hide_style = """
<style>

/* HIDE STREAMLIT DEFAULT */

#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

header {
    visibility: hidden;
}

/* HIDE OLD SIDEBAR PAGES */

section[data-testid="stSidebarNav"] ul {
    display: none;
}

</style>
"""

st.markdown(
    hide_style,
    unsafe_allow_html=True
)

# =========================
# SIDEBAR TITLE
# =========================

st.sidebar.markdown("""
<h1 style='
text-align:center;
color:white;
font-size:34px;
margin-bottom:30px;
'>
""", unsafe_allow_html=True)


# =========================
# HERO CARD
# =========================

st.markdown("""
<div style="
background: rgba(0,0,0,0.70);
padding:50px;
border-radius:25px;
text-align:center;
margin-top:20px;
margin-bottom:40px;
backdrop-filter: blur(8px);
">

<h1 style="
color:white;
font-size:28px;
margin-bottom:10px;
">
🩺 AI Health Consultant
</h1>

<p style="
color:white;
font-size:14px;
font-weight:bold;
">
AI Driven Health Consultant & Disease Prediction System
</p>

</div>
""", unsafe_allow_html=True)
# =========================
# CARDS
# =========================

show_cards()

# =========================
# MAIN CONTENT
# =========================

st.markdown("""

# 🧠 Smart AI Disease Prediction System

Welcome to the next-generation AI-powered health consultant.

This system uses Machine Learning to predict diseases based on symptoms and provides intelligent medical recommendations.

---

## 🚀 Features

✅ 70 Disease Detection

✅ AI-Based Disease Prediction

✅ PDF Medical Reports

✅ Specialist Recommendation

✅ Prediction Analytics

✅ Login & Register System

✅ Admin Dashboard

✅ Prediction History

✅ Smart Confidence Score

---

## 🎯 Project Objective

To build an intelligent healthcare assistant that helps users analyze symptoms and receive AI-powered disease predictions.

""")

# =========================
# FOOTER
# =========================

st.markdown("---")

st.markdown("""
<div style="
text-align:center;
color:white;
font-size:18px;
padding:20px;
">

© 2026 AI Health Consultant

<br><br>

Final Year Project

<br>
            
Designed & Developed by JUT CSE 2023

</div>
""", unsafe_allow_html=True)