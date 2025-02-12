import joblib

# Load the trained model
model = joblib.load("models/ids_model.pkl")

def detect_anomalies(features):
    prediction = model.predict([features])
    if prediction[0] == 1:
        print(f"[ALERT] Anomalous activity detected: {features}")
