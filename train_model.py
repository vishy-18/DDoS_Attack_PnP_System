import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

X_train = pd.read_csv('X_train.csv')
y_train = pd.read_csv('y_train.csv')

model = RandomForestClassifier()
model.fit(X_train, y_train.values.ravel())

joblib.dump(model, 'ddos_model.pkl')
print("✅ Model saved as ddos_model.pkl")
