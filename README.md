# JAR-Based Scoring Model Migration (GCP)

This project contains a JAR-based machine learning scoring model intended for migration and deployment to Google Cloud Platform (GCP).

---

## 🚀 Run the JAR for Inference

Use the following command to run the JAR file and generate predictions from your input CSV data:

```bash
java -jar target/score-model-1.0-jar-with-dependencies.jar model/data.csv predictions.csv
