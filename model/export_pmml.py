# export_pmml.py
import pandas as pd
from sklearn.datasets import fetch_openml
from sklearn.linear_model import LinearRegression
from sklearn2pmml import PMMLPipeline, sklearn2pmml

# Load data and train again (since you already have data.csv)
data = fetch_openml(name="boston", version=1, as_frame=True)
df = data.frame
X = df.drop(columns=["MEDV"])
y = df["MEDV"]

pipeline = PMMLPipeline([
    ("regressor", LinearRegression())
])
pipeline.fit(X, y)

# Export to PMML
sklearn2pmml(pipeline, "linear_model.pmml", with_repr=True)

print("✅ Exported PMML to linear_model.pmml")
