import streamlit as st
import streamlit.components.v1 as components

# =========================
# PAGE CONFIG
# =========================

st.set_page_config(
    page_title="Nearby Hospitals",
    page_icon="🏥",
    layout="wide"
)

# =========================
# PAGE TITLE
# =========================

st.title("🏥 Nearby Hospitals Locator")

st.write(
    "Find specialist hospitals near your location based on disease."
)

# =========================
# CITY INPUT
# =========================

city = st.text_input(
    "📍 Enter Your City",
    "Lahore"
)

# =========================
# DISEASE SELECTION
# =========================

disease = st.selectbox(
    "Select Disease",
    [
        "Heart Attack",
        "Diabetes",
        "Asthma",
        "Migraine",
        "Kidney Stones",
        "Skin Allergy",
        "Fungal infection",
        "GERD",
        "Depression",
        "Eye Infection",
        "Arthritis",
        "Liver Disease",
        "Typhoid",
        "Hypertension",
        "Pneumonia"
    ]
)

# =========================
# HOSPITAL SEARCH MAPPING
# =========================

hospital_mapping = {

    "Heart Attack": "Cardiology Hospital",
    "Hypertension": "Cardiology Hospital",

    "Diabetes": "Diabetes Specialist Hospital",

    "Asthma": "Pulmonology Hospital",
    "Pneumonia": "Pulmonology Hospital",

    "Migraine": "Neurology Hospital",

    "Kidney Stones": "Nephrology Hospital",

    "Skin Allergy": "Dermatology Hospital",
    "Fungal infection": "Dermatology Hospital",

    "GERD": "Gastroenterology Hospital",

    "Depression": "Psychiatry Hospital",

    "Eye Infection": "Eye Hospital",

    "Arthritis": "Orthopedic Hospital",

    "Liver Disease": "Liver Specialist Hospital",

    "Typhoid": "Infectious Disease Hospital"
}

# =========================
# SEARCH QUERY
# =========================

hospital_search = hospital_mapping.get(
    disease,
    "Hospital"
)

search_query = f"{hospital_search} in {city}"

maps_url = (
    f"https://www.google.com/maps/search/{search_query.replace(' ', '+')}"
)

# =========================
# SHOW RESULT
# =========================

st.success(
    f"Recommended specialist hospitals for {disease}"
)

st.link_button(
    "🏥 Open Hospitals in Google Maps",
    maps_url
)

# =========================
# EMBED MAP
# =========================

st.subheader("🗺️ Hospital Map")

map_url = (
    f"https://maps.google.com/maps?q={search_query.replace(' ', '+')}"
    "&t=&z=13&ie=UTF8&iwloc=&output=embed"
)

components.iframe(
    map_url,
    height=600,
    scrolling=True
)

# =========================
# SPECIALIST INFO
# =========================

st.subheader("👨‍⚕️ Recommended Specialist")

specialist_mapping = {

    "Heart Attack": "Cardiologist",
    "Hypertension": "Cardiologist",

    "Diabetes": "Endocrinologist",

    "Asthma": "Pulmonologist",
    "Pneumonia": "Pulmonologist",

    "Migraine": "Neurologist",

    "Kidney Stones": "Nephrologist",

    "Skin Allergy": "Dermatologist",
    "Fungal infection": "Dermatologist",

    "GERD": "Gastroenterologist",

    "Depression": "Psychiatrist",

    "Eye Infection": "Ophthalmologist",

    "Arthritis": "Orthopedic Specialist",

    "Liver Disease": "Hepatologist",

    "Typhoid": "Infectious Disease Specialist"
}

specialist = specialist_mapping.get(
    disease,
    "General Physician"
)

st.info(
    f"👨‍⚕️ Suggested Specialist: {specialist}"
)