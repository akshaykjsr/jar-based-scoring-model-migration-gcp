# score.py
import pandas as pd
import joblib
import sys

def main(input_file, output_file):
    model = joblib.load("model/linear_model.pkl")
    df = pd.read_csv(input_file)
    preds = model.predict(df)
    pd.DataFrame(preds, columns=["Prediction"]).to_csv(output_file, index=False)

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
