import streamlit as st
import pandas as pd
import joblib
import sqlite3
import os
from utils.style import load_css
from utils.recommendation import get_recommendation
from utils.pdf_report import generate_pdf_report

# =========================
# USER SESSION
# =========================

username = st.session_state.get(
    "username",
    "Guest User"
)

# =========================
# PAGE CONFIG
# =========================

st.set_page_config(
    page_title="Disease Prediction",
    page_icon="🩺",
    layout="wide"
)

# =========================
# LOAD CSS
# =========================

load_css()
BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

model_path = os.path.join(
    BASE_DIR,
    "model.pkl"
)

encoder_path = os.path.join(
    BASE_DIR,
    "label_encoder.pkl"
)

model = joblib.load(model_path)

label_encoder = joblib.load(
    encoder_path
)
# =========================
# DATABASE CONNECTION
# =========================

conn = sqlite3.connect(
    "database/health.db"
)

cursor = conn.cursor()

# =========================
# TITLE
# =========================

st.markdown("""
<h1 style='color:white; text-align:center;'>
🩺 AI Disease Prediction System
</h1>
""", unsafe_allow_html=True)

st.markdown("""
<p style='color:white; text-align:center; font-size:20px;'>
Select symptoms and predict disease.
</p>
""", unsafe_allow_html=True)

# =========================
# SYMPTOMS LIST
# =========================

symptoms = [
    'itching', 'skin_rash',
    'nodal_skin_eruptions',
    'continuous_sneezing',
    'shivering', 'chills',
    'joint_pain', 'stomach_pain',
    'acidity',
    'ulcers_on_tongue',
    'muscle_wasting',
    'vomiting',
    'burning_micturition',
    'spotting_urination',
    'fatigue',
    'weight_gain',
    'anxiety',
    'cold_hands_and_feets',
    'mood_swings',
    'weight_loss',
    'restlessness',
    'lethargy',
    'patches_in_throat',
    'irregular_sugar_level',
    'cough',
    'high_fever',
    'sunken_eyes',
    'breathlessness',
    'sweating',
    'dehydration',
    'indigestion',
    'headache',
    'yellowish_skin',
    'dark_urine',
    'nausea',
    'loss_of_appetite',
    'pain_behind_the_eyes',
    'back_pain',
    'constipation',
    'abdominal_pain',
    'diarrhoea',
    'mild_fever',
    'yellow_urine',
    'yellowing_of_eyes',
    'acute_liver_failure',
    'fluid_overload',
    'swelling_of_stomach',
    'swelled_lymph_nodes',
    'malaise',
    'blurred_and_distorted_vision',
    'phlegm',
    'throat_irritation',
    'redness_of_eyes',
    'sinus_pressure',
    'runny_nose',
    'congestion',
    'chest_pain',
    'weakness_in_limbs',
    'fast_heart_rate',
    'pain_during_bowel_movements',
    'pain_in_anal_region',
    'bloody_stool',
    'irritation_in_anus',
    'neck_pain',
    'dizziness',
    'cramps',
    'bruising',
    'obesity',
    'swollen_legs',
    'swollen_blood_vessels',
    'puffy_face_and_eyes',
    'enlarged_thyroid',
    'brittle_nails',
    'swollen_extremeties',
    'excessive_hunger',
    'drying_and_tingling_lips',
    'slurred_speech',
    'knee_pain',
    'hip_joint_pain',
    'muscle_weakness',
    'stiff_neck',
    'swelling_joints',
    'movement_stiffness',
    'spinning_movements',
    'loss_of_balance',
    'unsteadiness',
    'weakness_of_one_body_side',
    'loss_of_smell',
    'bladder_discomfort',
    'foul_smell_of_urine',
    'continuous_feel_of_urine',
    'passage_of_gases',
    'internal_itching',
    'depression',
    'irritability',
    'muscle_pain',
    'altered_sensorium',
    'red_spots_over_body',
    'belly_pain',
    'abnormal_menstruation'
]

# =========================
# USER INPUT
# =========================

selected_symptoms = []

st.markdown("""
<h3 style='color:white;'>
Select Symptoms
</h3>
""", unsafe_allow_html=True)

cols = st.columns(3)

for index, symptom in enumerate(symptoms):

    with cols[index % 3]:

        if st.checkbox(
            symptom.replace(
                "_",
                " "
            ).title()
        ):

            selected_symptoms.append(
                symptom
            )
# =========================
# BUTTON STYLING
# =========================

st.markdown("""
<style>

/* Predict Button */

div.stButton > button {
    background: #007BFF;
    color: white;
    font-size: 20px;
    font-weight: bold;
    border-radius: 12px;
    padding: 12px 30px;
    border: none;
    width: 100%;
}

/* Hover Effect */

div.stButton > button:hover {
    background: #0056D2;
    color: white;
}

/* Download PDF Button */

div.stDownloadButton > button {
    background: #007BFF;
    color: white;
    font-size: 18px;
    font-weight: bold;
    border-radius: 12px;
    padding: 12px 25px;
    border: none;
    width: 100%;
}

/* Hover */

div.stDownloadButton > button:hover {
    background: #0056D2;
    color: white;
}

</style>
""", unsafe_allow_html=True)
# =========================
# PREDICT BUTTON
# =========================

if st.button("🔍 Predict Disease"):

    input_data = {}

    for symptom in symptoms:

        input_data[symptom] = (
            1 if symptom in selected_symptoms
            else 0
        )

    input_df = pd.DataFrame(
        [input_data]
    )

    # =========================
    # MODEL PREDICTION
    # =========================

    prediction = model.predict(
        input_df
    )

    probabilities = (
        model.predict_proba(input_df)
    )

    confidence = (
        max(probabilities[0]) * 100
    )

    predicted_disease = (
        label_encoder
        .inverse_transform(prediction)[0]
    )

    # =========================
    # RECOMMENDATION
    # =========================

    recommendation = (
        get_recommendation(
            predicted_disease
        )
    )

    # =========================
    # SHOW RESULTS
    # =========================

    st.success(
        f"Predicted Disease: "
        f"{predicted_disease}"
    )

    st.info(
        f"👨‍⚕️ Specialist: "
        f"{recommendation['specialist']}"
    )

    st.info(
        f"💊 Medicine: "
        f"{recommendation['medicine']}"
    )

    st.info(
        f"🥗 Diet: "
        f"{recommendation['diet']}"
    )

    st.info(
        f"⚠️ Precaution: "
        f"{recommendation['precaution']}"
    )

    st.info(
        f"📊 Confidence Score: "
        f"{confidence:.2f}%"
    )

    # =========================
    # SAVE HISTORY
    # =========================

    symptoms_text = ", ".join(
        selected_symptoms
    )

    cursor.execute(
        """
        INSERT INTO history (
            username,
            disease,
            confidence,
            symptoms
        )
        VALUES (?, ?, ?, ?)
        """,
        (
            username,
            predicted_disease,
            confidence,
            symptoms_text
        )
    )

    conn.commit()

    # =========================
    # GENERATE PDF
    # =========================

    pdf_file = generate_pdf_report(
        predicted_disease,
        confidence,
        recommendation['specialist'],
        symptoms_text
    )

    # =========================
    # DOWNLOAD BUTTON
    # =========================

    with open(pdf_file, "rb") as file:

        st.download_button(
            label="📄 Download Medical Report",
            data=file,
            file_name="medical_report.pdf",
            mime="application/pdf"
        )

    st.warning(
        "⚠️ This system is for educational purposes only."
    )
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