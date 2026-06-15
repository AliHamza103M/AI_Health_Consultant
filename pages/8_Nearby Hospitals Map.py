# =========================
# HOSPITAL RECOMMENDATION
# =========================

st.subheader("🏥 Nearby Hospitals")

if predicted_disease == "Heart Attack":
    hospital_search = "Cardiology Hospital Near Me"

elif predicted_disease == "Diabetes":
    hospital_search = "Diabetes Specialist Hospital Near Me"

elif predicted_disease == "Asthma":
    hospital_search = "Pulmonology Hospital Near Me"

elif predicted_disease == "Migraine":
    hospital_search = "Neurology Hospital Near Me"

elif predicted_disease == "Kidney Stones":
    hospital_search = "Nephrology Hospital Near Me"

elif predicted_disease == "Skin Allergy":
    hospital_search = "Dermatology Hospital Near Me"

else:
    hospital_search = "Hospital Near Me"

google_maps_url = (
    f"https://www.google.com/maps/search/{hospital_search}"
)

st.info(
    "Click the button below to view nearby hospitals on Google Maps."
)

st.link_button(
    "🏥 View Nearby Hospitals",
    google_maps_url
)
st.subheader("🗺 Hospital Map")

st.components.v1.iframe(
    "https://maps.google.com/maps?q=hospital&t=&z=13&ie=UTF8&iwloc=&output=embed",
    height=450
)