from flask import Flask, render_template, request, send_file
import pandas as pd
import joblib

app = Flask(__name__)

# Load model
model = joblib.load("fraud_model.pkl")

# Load dataset
data = pd.read_csv("Cleaned_DataSet_V3.csv")

# Convert text columns
text_columns = data.select_dtypes(include=["object", "str"]).columns

for col in text_columns:
    data[col] = data[col].astype("category").cat.codes

# Features
X = data.drop(["F3912", "F3924"], axis=1)

# Statistics
TOTAL_TRANSACTIONS = len(data)
FRAUD_COUNT = int(data["F3912"].sum())
NORMAL_COUNT = TOTAL_TRANSACTIONS - FRAUD_COUNT

# History
history = []

@app.route("/", methods=["GET", "POST"])
def home():

    result = ""
    risk = ""
    row_value = ""

    if request.method == "POST":

        try:

            row_value = request.form["row"]

            row = int(row_value)

            sample = X.loc[[row]]

            prediction = model.predict(sample)

            if prediction[0] == 1:

                result = "🚨 Fraud Detected"
                risk = "🔴 HIGH RISK"

            else:

                result = "✅ Normal Transaction"
                risk = "🟢 LOW RISK"

            history.insert(0, {
                "row": row,
                "result": result,
                "risk": risk
            })

        except:

            result = "Invalid Transaction ID"

    return render_template(
        "index.html",
        result=result,
        risk=risk,
        row_value=row_value,
        history=history[:10],
        total=TOTAL_TRANSACTIONS,
        fraud=FRAUD_COUNT,
        normal=NORMAL_COUNT
    )

@app.route("/download")
def download():

    df = pd.DataFrame(history)

    file_name = "prediction_history.csv"

    df.to_csv(file_name, index=False)

    return send_file(
        file_name,
        as_attachment=True
    )

if __name__ == "__main__":
    app.run(debug=True)