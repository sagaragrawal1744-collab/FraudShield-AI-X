import pandas as pd

data = pd.read_csv("Cleaned_DataSet.csv")

missing_percentage = (data.isnull().sum() / len(data)) * 100

cleaned_data_v2 = data.loc[:, missing_percentage <= 90]

print("Original Shape:", data.shape)
print("New Shape:", cleaned_data_v2.shape)

cleaned_data_v2.to_csv("Cleaned_DataSet_V2.csv", index=False)

print("Second cleaned dataset created successfully!")