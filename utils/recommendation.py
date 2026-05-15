def get_recommendation(disease):

    recommendations = {

        "Fungal infection": {
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
        }

    }

    default_data = {
        "specialist": "General Doctor",
        "medicine": "Consult Doctor",
        "diet": "Healthy Diet",
        "precaution": "Regular Checkup"
    }

    return recommendations.get(
        disease,
        default_data
    )