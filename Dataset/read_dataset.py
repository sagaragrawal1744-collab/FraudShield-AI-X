import pandas as pd

data = pd.read_csv("Cleaned_DataSet_V2.csv")

# Fill numeric columns with median
numeric_columns = data.select_dtypes(include=["float64", "int64"]).columns

for col in numeric_columns:
    data[col] = data[col].fillna(data[col].median())

# Fill text columns with mode
text_columns = data.select_dtypes(include=["object", "str"]).columns

for col in text_columns:
    data[col] = data[col].fillna(data[col].mode()[0])

print("Remaining Missing Values:")
print(data.isnull().sum().sum())

data.to_csv("Cleaned_DataSet_V3.csv", index=False)

print("Final model-ready dataset created!")