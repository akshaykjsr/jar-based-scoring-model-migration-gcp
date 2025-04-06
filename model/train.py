# train.py
import pandas as pd
from sklearn.datasets import fetch_openml
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import joblib

# Load dataset from openml
data = fetch_openml(name="boston", version=1, as_frame=True)
df = data.frame

# Features and target
X = df.drop(columns=["MEDV"])
y = df["MEDV"]

# Split (optional, just for demo)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Save model
joblib.dump(model, "linear_model.pkl")

# Save test set to CSV for scoring
X_test.to_csv("data.csv", index=False)

print("✅ Model trained and saved as 'linear_model.pkl'")
print("✅ Sample data saved as 'data.csv'")
