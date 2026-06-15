from flask import Flask, render_template, request
import pandas as pd
import joblib

app = Flask(__name__)

model = joblib.load("fraud_model.pkl")

data = pd.read_csv("Cleaned_DataSet_V3.csv")

text_columns = data.select_dtypes(include=["object", "str"]).columns

for col in text_columns:
    data[col] = data[col].astype("category").cat.codes

X = data.drop(["F3912", "F3924"], axis=1)

@app.route("/", methods=["GET", "POST"])
def home():

    result = ""
    row_value = ""

    if request.method == "POST":

        row_value = request.form["row"]

        row = int(row_value)

        sample = X.loc[[row]]

        prediction = model.predict(sample)

        if prediction[0] == 1:
            result = "🚨 Fraud Detected"
        else:
            result = "✅ Normal Transaction"

    return render_template(
        "index.html",
        result=result,
        row_value=row_value
    )

if __name__ == "__main__":
    app.run(debug=True)
