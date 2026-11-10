import pandas as pd
import numpy as np

# Load renewable energy dataset
df = pd.read_csv("Renewable.csv")

# 1. Dataset dimensions
print("Dataset Shape:")
print(df.shape)

# 2. Column names
print("\nColumn Names:")
print(df.columns.tolist())

# 3. Data types
print("\nData Types:")
print(df.dtypes)

# 4. First five records
print("\nFirst 5 Rows:")
print(df.head())

# 5. Statistical summary
print("\nStatistical Summary:")
print(df.describe())