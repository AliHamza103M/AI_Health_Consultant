from utils.style import load_css
import streamlit as st
import sqlite3

# =========================
# PAGE CONFIG
# =========================

st.set_page_config(
    page_title="Register",
    page_icon="📝",
    layout="centered"
)

load_css()

# =========================
# DATABASE CONNECTION
# =========================

conn = sqlite3.connect("database/health.db")

cursor = conn.cursor()

# =========================
# PAGE TITLE
# =========================

st.title("📝 User Registration")

st.write("Create your account")

# =========================
# INPUT FIELDS
# =========================

username = st.text_input("Username")

email = st.text_input("Email")

password = st.text_input("Password", type="password")

confirm_password = st.text_input("Confirm Password", type="password")

# =========================
# REGISTER BUTTON
# =========================

if st.button("Register"):

    # VALIDATION
    if username == "" or email == "" or password == "":

        st.error("All fields are required")

    elif password != confirm_password:

        st.error("Passwords do not match")

    else:

        try:

            cursor.execute(
                """
                INSERT INTO users (username, email, password)
                VALUES (?, ?, ?)
                """,
                (username, email, password)
            )

            conn.commit()

            st.success("Registration Successful ✅")

        except:

            st.error("Email already exists")