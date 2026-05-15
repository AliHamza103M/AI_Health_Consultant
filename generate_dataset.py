import pandas as pd
import random

# =========================
# SYMPTOMS LIST
# =========================

symptoms = [
    'itching', 'skin_rash', 'nodal_skin_eruptions', 'continuous_sneezing',
    'shivering', 'chills', 'joint_pain', 'stomach_pain', 'acidity',
    'ulcers_on_tongue', 'muscle_wasting', 'vomiting', 'burning_micturition',
    'spotting_urination', 'fatigue', 'weight_gain', 'anxiety',
    'cold_hands_and_feets', 'mood_swings', 'weight_loss', 'restlessness',
    'lethargy', 'patches_in_throat', 'irregular_sugar_level', 'cough',
    'high_fever', 'sunken_eyes', 'breathlessness', 'sweating', 'dehydration',
    'indigestion', 'headache', 'yellowish_skin', 'dark_urine', 'nausea',
    'loss_of_appetite', 'pain_behind_the_eyes', 'back_pain', 'constipation',
    'abdominal_pain', 'diarrhoea', 'mild_fever', 'yellow_urine',
    'yellowing_of_eyes', 'acute_liver_failure', 'fluid_overload',
    'swelling_of_stomach', 'swelled_lymph_nodes', 'malaise',
    'blurred_and_distorted_vision', 'phlegm', 'throat_irritation',
    'redness_of_eyes', 'sinus_pressure', 'runny_nose', 'congestion',
    'chest_pain', 'weakness_in_limbs', 'fast_heart_rate',
    'pain_during_bowel_movements', 'pain_in_anal_region', 'bloody_stool',
    'irritation_in_anus', 'neck_pain', 'dizziness', 'cramps', 'bruising',
    'obesity', 'swollen_legs', 'swollen_blood_vessels', 'puffy_face_and_eyes',
    'enlarged_thyroid', 'brittle_nails', 'swollen_extremeties',
    'excessive_hunger', 'drying_and_tingling_lips',
    'slurred_speech', 'knee_pain', 'hip_joint_pain', 'muscle_weakness',
    'stiff_neck', 'swelling_joints', 'movement_stiffness',
    'spinning_movements', 'loss_of_balance', 'unsteadiness',
    'weakness_of_one_body_side', 'loss_of_smell', 'bladder_discomfort',
    'foul_smell_of_urine', 'continuous_feel_of_urine', 'passage_of_gases',
    'internal_itching', 'depression', 'irritability',
    'muscle_pain', 'altered_sensorium', 'red_spots_over_body',
    'belly_pain', 'abnormal_menstruation'
]

# =========================
# 70 DISEASES
# =========================

Diseases = [
    'Fungal infection', 'Allergy', 'GERD', 'Chronic cholestasis',
    'Drug Reaction', 'Peptic ulcer disease', 'AIDS', 'Diabetes',
    'Gastroenteritis', 'Bronchial Asthma', 'Hypertension', 'Migraine',
    'Cervical spondylosis', 'Paralysis', 'Jaundice',
    'Malaria', 'Chicken pox', 'Dengue', 'Typhoid', 'Hepatitis A',
    'Hepatitis B', 'Hepatitis C', 'Hepatitis D', 'Hepatitis E',
    'Alcoholic hepatitis', 'Tuberculosis', 'Common Cold', 'Pneumonia',
    'Hemorrhoids', 'Heart attack', 'Varicose veins',
    'Hypothyroidism', 'Hyperthyroidism', 'Hypoglycemia', 'Osteoarthritis',
    'Arthritis', 'Vertigo', 'Acne', 'Urinary tract infection',
    'Psoriasis', 'Impetigo', 'COVID-19', 'Flu', 'Sinusitis',
    'Anemia', 'Depression', 'Epilepsy', 'Parkinsons', 'Alzheimer',
    'Stroke', 'Kidney stones', 'Liver disease', 'Pancreatitis',
    'Appendicitis', 'Food poisoning', 'Asthma', 'Heart disease',
    'Obesity', 'High cholesterol', 'Low blood pressure',
    'High blood pressure', 'Skin cancer', 'Lung cancer',
    'Colon cancer', 'Breast cancer', 'Brain tumor',
    'Chronic kidney disease', 'Sleep apnea', 'Anxiety disorder'
]

# =========================
# GENERATE DATA
# =========================

rows = []

for disease in Diseases:

    for _ in range(80):

        row = {}

        for symptom in symptoms:
            row[symptom] = random.choice([0, 1])

        row['Disease'] = disease

        rows.append(row)

# =========================
# CREATE DATAFRAME
# =========================

print("Creating dataset...")

DF = pd.DataFrame(rows)

# =========================
# SAVE DATASET
# =========================

DF.to_csv('dataset/dataset.csv', index=False)

print("Dataset Created Successfully")
print("Total Rows:", DF.shape[0])
print("Total Columns:", DF.shape[1])
print("Dataset saved to dataset/dataset.csv")