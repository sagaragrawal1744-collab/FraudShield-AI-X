import matplotlib.pyplot as plt

labels = ["Normal", "Fraud"]
values = [9001, 81]

plt.figure(figsize=(6,6))
plt.pie(values, labels=labels, autopct="%1.1f%%")
plt.title("Fraud Distribution")

plt.savefig("static/charts/fraud_pie.png")

print("Chart created successfully!")