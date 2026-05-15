import pandas as pd
import numpy as np
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix


print("Loading dataset...")

# =========================
# LOAD DATASET
# =========================

df = pd.read_csv("dataset/dataset.csv")

print("\nDataset Loaded Successfully")
print(df.head())


# =========================
# DATASET INFO
# =========================

print("\nDataset Shape:")
print(df.shape)

print("\nDataset Columns:")
print(df.columns)


# =========================
# CHECK NULL VALUES
# =========================

print("\nMissing Values:")
print(df.isnull().sum())


# =========================
# TARGET COLUMN
# =========================

# If your dataset uses prognosis instead of Disease,
# replace Disease with prognosis

TARGET_COLUMN = 'Disease'

# =========================
# FEATURES & LABELS
# =========================

X = df.drop(TARGET_COLUMN, axis=1)
y = df[TARGET_COLUMN]


# =========================
# LABEL ENCODING
# =========================

label_encoder = LabelEncoder()
y_encoded = label_encoder.fit_transform(y)


# =========================
# TRAIN TEST SPLIT
# =========================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y_encoded,
    test_size=0.2,
    random_state=42,
    stratify=y_encoded
)

print("\nTraining Samples:", X_train.shape[0])
print("Testing Samples:", X_test.shape[0])


# =========================
# RANDOM FOREST MODEL
# =========================

print("\nTraining Random Forest Model...")

model = RandomForestClassifier(
    n_estimators=300,
    max_depth=25,
    random_state=42
)

model.fit(X_train, y_train)


# =========================
# PREDICTIONS
# =========================

predictions = model.predict(X_test)


# =========================
# ACCURACY
# =========================

accuracy = accuracy_score(y_test, predictions)

print("\n=========================")
print(f"Model Accuracy: {accuracy * 100:.2f}%")
print("=========================\n")


# =========================
# CLASSIFICATION REPORT
# =========================

print("Classification Report:\n")
print(classification_report(y_test, predictions))


# =========================
# CONFUSION MATRIX
# =========================

cm = confusion_matrix(y_test, predictions)

print("Confusion Matrix Shape:")
print(cm.shape)


# =========================
# SAVE MODEL
# =========================

joblib.dump(model, 'model.pkl')
joblib.dump(label_encoder, 'label_encoder.pkl')

print("\nModel Saved Successfully")
print("Files Created:")
print("- model.pkl")
print("- label_encoder.pkl")


# =========================
# SAMPLE PREDICTION TEST
# =========================

sample_prediction = model.predict(X_test.iloc[:1])

predicted_disease = label_encoder.inverse_transform(sample_prediction)

print("\nSample Prediction:")
print(predicted_disease)
