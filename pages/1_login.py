from utils.style import load_css
import streamlit as st
import sqlite3

# =========================
# PAGE CONFIG
# =========================

st.set_page_config(
    page_title="Login",
    page_icon="🔐",
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

st.title("🔐 User Login")

st.write("Login to continue")

# =========================
# INPUT FIELDS
# =========================

email = st.text_input("Email")

password = st.text_input(
    "Password",
    type="password"
)

# =========================
# LOGIN BUTTON
# =========================

if st.button("Login"):

    cursor.execute(
        """
        SELECT * FROM users
        WHERE email = ? AND password = ?
        """,
        (email, password)
    )

    user = cursor.fetchone()

    # =========================
    # LOGIN SUCCESS
    # =========================

    if user:

        st.success("Login Successful ✅")

        # SAVE SESSION

        st.session_state["username"] = user[1]

        st.session_state["email"] = user[2]

        # =========================
        # ADMIN ACCESS
        # =========================

        ADMIN_EMAIL = "alihamza@gmail.com"

        if email == ADMIN_EMAIL:

            st.session_state["is_admin"] = True

        else:

            st.session_state["is_admin"] = False

        st.balloons()

        st.write(f"Welcome, {user[1]}")

    # =========================
    # LOGIN FAILED
    # =========================

    else:

        st.error("Invalid Email or Password")