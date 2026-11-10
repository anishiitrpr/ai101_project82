import pandas as pd
import numpy as np

df = pd.read_csv("Renewable.csv")

print("Dataset Shape:")
print(df.shape)

print("\nColumn Names:")
print(df.columns.tolist())

print("\nData Types:")
print(df.dtypes)


print("\nFirst 5 Rows:")
print(df.head())


print("\nStatistical Summary:")
print(df.describe())


#  STATISTICAL ANALYSIS


print("\n" + "=" * 50)
print("STATISTICAL ANALYSIS")
print("=" * 50)


numeric_df = df.select_dtypes(include="number")

print("\nNumerical Columns:")
print(numeric_df.columns.tolist())


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


print("\nMissing Values:")
print(df.isnull().sum())

print("\nStatistical Analysis Completed!")


# renewable energy and weather comparisons
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

import os

os.makedirs("results", exist_ok=True)

numeric_cols = df.select_dtypes(include="number").columns.tolist()
categorical_cols = df.select_dtypes(include="object").columns.tolist()

sns.set_theme(style="whitegrid")

print("\n--- FINAL DATA ANALYSIS ---")

#  Correlation Analysis
if len(numeric_cols) >= 2:
    corr = df[numeric_cols].corr()

    print("\nCorrelation Matrix:")
    print(corr.round(2))

    # Heatmap
    plt.figure(figsize=(10, 6))
    sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f")
    plt.title("Renewable Energy and Weather Correlation")
    plt.tight_layout()
    plt.savefig("results/correlation_heatmap.png")
    plt.close()

   # Weather vs Energy Output Comparisons

energy_col = next(
    (c for c in df.columns
     if "energy" in c.lower() and "wh" in c.lower()),
    None
)

weather_cols = [
    c for c in ["GHI", "temp", "humidity", "wind_speed"]
    if c in df.columns
]

if energy_col:
    for col in weather_cols:
        plt.figure(figsize=(7, 5))

        sns.regplot(
            data=df,
            x=col,
            y=energy_col,
            scatter_kws={"alpha": 0.4, "s": 15}
        )

        plt.title(f"Energy Output vs {col}")
        plt.tight_layout()

        plt.savefig(f"results/energy_vs_{col}.png")
        plt.close()

        print(
            f"Correlation between {energy_col} and {col}:",
            round(df[energy_col].corr(df[col]), 3)
        )

#  Monthly Energy Output Comparison

if energy_col and "month" in df.columns:
    monthly = df.groupby("month")[energy_col].mean()

    plt.figure(figsize=(9, 5))
    monthly.plot(kind="bar")

    plt.title("Average Renewable Energy Output by Month")
    plt.xlabel("Month")
    plt.ylabel("Average Energy Output (Wh)")
    plt.xticks(rotation=0)

    plt.tight_layout()
    plt.savefig("results/monthly_energy_comparison.png")
    plt.close()

    print("\nMonthly Energy Output:")
    print(monthly.round(2))

#  Renewable Energy Source Comparison
source_col = next(
    (c for c in categorical_cols
     if any(word in c.lower()
            for word in ["source", "type", "energy", "renewable"])),
    None
)

if source_col and numeric_cols:
    value_col = numeric_cols[0]

    comparison = df.groupby(source_col)[value_col].mean().sort_values(
        ascending=False
    )

    print("\nEnergy Source Comparison:")
    print(comparison)

    plt.figure(figsize=(9, 5))
    comparison.plot(kind="bar")
    plt.title(f"Average {value_col} by {source_col}")
    plt.ylabel(f"Average {value_col}")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("results/energy_comparison.png")
    plt.close()

#  Energy Production Trend
time_col = next(
    (c for c in df.columns
     if any(word in c.lower() for word in ["year", "date"])),
    None
)

if time_col and numeric_cols:
    trend = df.groupby(time_col)[numeric_cols[0]].mean()

    plt.figure(figsize=(9, 5))
    trend.plot(kind="line", marker="o")
    plt.title(f"{numeric_cols[0]} Trend Over Time")
    plt.xlabel(time_col)
    plt.ylabel(numeric_cols[0])
    plt.tight_layout()
    plt.savefig("results/energy_trend.png")
    plt.close()

#  Final Output
print("\nGraphs saved successfully in the results folder.")
print("Available numerical columns:", numeric_cols)
print("Available categorical columns:", categorical_cols)