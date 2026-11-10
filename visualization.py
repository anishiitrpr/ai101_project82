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


#  STATISTICAL ANALYSIS


print("\n" + "=" * 50)
print("STATISTICAL ANALYSIS")
print("=" * 50)

# Select all numerical columns
numeric_df = df.select_dtypes(include="number")

print("\nNumerical Columns:")
print(numeric_df.columns.tolist())

# Calculate statistical measures
if not numeric_df.empty:

    statistics = pd.DataFrame({
        "Mean": numeric_df.mean(),
        "Median": numeric_df.median(),
        "Standard Deviation": numeric_df.std(),
        "Minimum": numeric_df.min(),
        "Maximum": numeric_df.max()
    })

    print("\nStatistical Summary:")
    print(statistics.round(2))

else:
    print("No numerical columns found.")

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

print("\nStatistical Analysis Completed!")
