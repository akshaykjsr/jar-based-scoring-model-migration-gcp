# score.py
import pandas as pd
import joblib

# Load model
model = joblib.load("linear_model.pkl")

# Load input CSV (large file)
data = pd.read_csv("data.csv")

# Predict
predictions = model.predict(data)

# Save results
output = pd.DataFrame(predictions, columns=["Predicted_MEDV"])
output.to_csv("predictions.csv", index=False)

print("✅ Predictions saved to 'predictions.csv'")

