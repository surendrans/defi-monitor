# ai_model.py
import pandas as pd
from sklearn.ensemble import IsolationForest

# Example: Load historical transaction data (you can replace this with real data)
transactions = pd.read_csv("historical_transactions.csv")

# Train a simple anomaly detection model
model = IsolationForest(contamination=0.01)  # Adjust contamination based on expected anomalies
model.fit(transactions[["value", "gas", "gasPrice"]])

def analyze_transaction(transaction):
    """
    Analyze a transaction and flag if it's suspicious.
    """
    # Extract relevant features
    features = pd.DataFrame([{
        "value": float(transaction.get("value", 0)),
        "gas": int(transaction.get("gas", 0)),
        "gasPrice": int(transaction.get("gasPrice", 0))
    }])

    # Predict if the transaction is an anomaly
    prediction = model.predict(features)
    if prediction == -1:
        print("🚨 Suspicious Transaction Detected:", transaction)
    else:
        print("✅ Normal Transaction:", transaction)