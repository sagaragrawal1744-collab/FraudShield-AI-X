import pandas as pd

data = pd.read_csv("DataSet.csv")

cleaned_data = data.dropna(axis=1, how="all")

cleaned_data.to_csv("Cleaned_DataSet.csv", index=False)

print("Cleaned dataset saved successfully!")
print("Shape:", cleaned_data.shape)