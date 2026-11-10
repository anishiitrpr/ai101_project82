import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("data/Renewable.csv")

print(df.head())
print(df.info())
print(df.columns)
print(df.shape)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Records:")
print(df.duplicated().sum())

print("\nStatistical Summary")
print(df.describe())

print("\nColumn Names")
print(df.columns.tolist())

print("\nData Types")
print(df.dtypes)

print("\nMissing Value")
print(df.isnull().sum().to_string())

print("\nFirst 10 Records")
print(df.head(10))

print("\nDuplicate Records")
print(df.duplicated().sum())

df = df.drop_duplicates()
print("\nDataset after removing duplicates:")
print(df.shape)

df['Time'] = pd.to_datetime(df['Time'])
df = df.sort_values(by='Time')
print("\nTime column converted successfully")
print(df['Time'].dtype)

print("\nFinal Dataset information:")
print(df.info())
print("\nFinal Dataset:")
print(df.head())

os.makedirs("data", exist_ok=True)
df.to_csv("data/cleaned_data.csv", index=False)
print("\nCleaned dataset saves susccesfully !")
print("Final dataset shape", df.shape)

print("\nMissing values after cleaning")
print(df.isnull().sum())
print("\nDuplicate records after cleaning ")
print(df.duplicated().sum())
print("\nFinal columns :")
print(df.columns.tolist())
print("\nFinal data shape:")
print(df.shape)

print("\n==================DATASET STRUCTURE===========")
print("\nAvailable Columns :")
print(df.columns.tolist())

print("\nColumn Data types :")
print(df.dtypes)

print("\nDataset preivew:")
print(df.head(10))

print("\nNumerical columns ")
print(df.select_dtypes(include=np.number).columns.tolist())

print("\nCategorical Columns:")
print(df.select_dtypes(include='object').columns.tolist())

if 'Time' in df.columns:
    df['Year'] = df["Time"].dt.year
    df['Month'] = df["Time"].dt.month
    df['Day'] = df["Time"].dt.day
    df['Hour'] = df["Time"].dt.hour
    print("\nTime feature created successfully")

print("\nupdated dataset:")
print(df.head())

print("\nupdated dataset shape:")
print(df.shape)

df.to_csv("data/feature_engineered_data.csv", index=False)
print("\nFeature engineered dataset savd successfully")
print("final shape", df.shape)

file_name = "data/cleaned_data.csv"

if os.path.exists(file_name):
    final_df = pd.read_csv(file_name)
    print("\n----- FINAL DATASET VALIDATION -----")
    print("File exists: Yes")
    print("Dataset loaded successfully")
    print("Rows:", final_df.shape[0])
    print("Columns:", final_df.shape[1])
    print("\nColumn names:")
    print(final_df.columns.tolist())
    print("\nMissing values:")
    print(final_df.isnull().sum())
    print("\nDuplicate rows:")
    print(final_df.duplicated().sum())
else:
    print("Error: Cleaned dataset not found!")