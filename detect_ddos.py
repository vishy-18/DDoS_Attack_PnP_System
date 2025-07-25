import pandas as pd
import joblib

# Load model
model = joblib.load('ddos_model.pkl')

# Load new sample data for detection
new_data = pd.read_csv('new_traffic.csv')
new_data = pd.get_dummies(new_data)

# Predict
predictions = model.predict(new_data)
print("Predictions (0: normal, 1: DDoS):", predictions)
