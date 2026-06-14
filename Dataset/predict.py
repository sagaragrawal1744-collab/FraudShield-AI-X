import pandas as pd
import joblib

model = joblib.load("fraud_model.pkl")

data = pd.read_csv("Cleaned_DataSet_V3.csv")

text_columns = data.select_dtypes(include=["object", "str"]).columns

for col in text_columns:
    data[col] = data[col].astype("category").cat.codes

X = data.drop(["F3912", "F3924"], axis=1)

row = int(input("Enter row number: "))

sample = X.loc[[row]]

prediction = model.predict(sample)

if prediction[0] == 1:
    print("🚨 Fraud Detected")
else:
    print("✅ Normal Transaction")