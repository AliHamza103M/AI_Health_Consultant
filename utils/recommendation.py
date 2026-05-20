def get_recommendation(disease):

    recommendations = {

        "Fungal Infection": {
            "specialist": "Dermatologist",
            "medicine": "Antifungal Cream",
            "diet": "Drink more water and avoid oily food",
            "precaution": "Maintain personal hygiene"
        },

        "Allergy": {
            "specialist": "Allergy Specialist",
            "medicine": "Antihistamines",
            "diet": "Avoid cold drinks and junk food",
            "precaution": "Avoid dust and allergens"
        },

        "GERD": {
            "specialist": "Gastroenterologist",
            "medicine": "Antacids",
            "diet": "Avoid spicy foods",
            "precaution": "Eat small meals"
        },

        "Diabetes": {
            "specialist": "Endocrinologist",
            "medicine": "Insulin / Metformin",
            "diet": "Low sugar diet",
            "precaution": "Exercise daily"
        },

        "Hypertension": {
            "specialist": "Cardiologist",
            "medicine": "Blood Pressure Medicine",
            "diet": "Low salt diet",
            "precaution": "Reduce stress"
        },

        "Heart Attack": {
            "specialist": "Cardiologist",
            "medicine": "Aspirin / Heart Medicines",
            "diet": "Low cholesterol diet",
            "precaution": "Avoid stress and smoking"
        },

        "Migraine": {
            "specialist": "Neurologist",
            "medicine": "Pain Relievers",
            "diet": "Avoid caffeine",
            "precaution": "Sleep properly"
        },

        "Asthma": {
            "specialist": "Pulmonologist",
            "medicine": "Inhaler",
            "diet": "Healthy warm foods",
            "precaution": "Avoid smoke and dust"
        },

        "Arthritis": {
            "specialist": "Orthopedic Specialist",
            "medicine": "Pain Relief Medicines",
            "diet": "Calcium rich diet",
            "precaution": "Daily light exercise"
        },

        "Kidney Stones": {
            "specialist": "Nephrologist",
            "medicine": "Pain Killers / Surgery",
            "diet": "Drink lots of water",
            "precaution": "Avoid soft drinks"
        },

        "Typhoid": {
            "specialist": "Infectious Disease Specialist",
            "medicine": "Antibiotics",
            "diet": "Boiled food and water",
            "precaution": "Maintain hygiene"
        },

        "Pneumonia": {
            "specialist": "Pulmonologist",
            "medicine": "Antibiotics",
            "diet": "Warm liquids",
            "precaution": "Avoid cold environment"
        },

        "Liver Disease": {
            "specialist": "Hepatologist",
            "medicine": "Liver Medicines",
            "diet": "Avoid oily foods",
            "precaution": "Avoid alcohol"
        },

        "Depression": {
            "specialist": "Psychiatrist",
            "medicine": "Therapy / Antidepressants",
            "diet": "Healthy diet",
            "precaution": "Stay socially active"
        },

        "Skin Allergy": {
            "specialist": "Dermatologist",
            "medicine": "Skin Cream",
            "diet": "Avoid allergic foods",
            "precaution": "Use clean clothes"
        },

        "Eye Infection": {
            "specialist": "Ophthalmologist",
            "medicine": "Eye Drops",
            "diet": "Vitamin A foods",
            "precaution": "Avoid touching eyes"
        }

    }

    default_data = {
        "specialist": "General Physician",
        "medicine": "Consult Doctor",
        "diet": "Healthy Diet",
        "precaution": "Regular Checkup"
    }

    # FIX CASE ISSUE
    disease = disease.strip().title()

    recommendations = {
        k.title(): v
        for k, v in recommendations.items()
    }

    return recommendations.get(
        disease,
        default_data
    )