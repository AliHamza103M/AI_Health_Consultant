import streamlit as st
from utils.cards import show_cards
from utils.database import create_tables
from utils.style import load_css
from header import show_header
# =========================
# PAGE CONFIG
# =========================

st.set_page_config(
    page_title="AI Health Consultant",
    page_icon="🩺",
    layout="wide"
)

# =========================
# LOAD CSS
# =========================

load_css()

# =========================
# CREATE DATABASE
# =========================

create_tables()

# =========================
# HEADER SECTION
# =========================

show_header()
show_cards()
# =========================
# HOME CONTENT
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

st.markdown(
    """
    <div style='text-align: center;'>

    © 2026 AI Health Consultant

    <br>

    Final Year Project

    </div>
    """,
    unsafe_allow_html=True
)