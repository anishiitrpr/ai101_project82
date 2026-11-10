#importing libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix

#loading the data and selecting the features
df = pd.read_csv("cleaned_data.csv")

# Detect weather features and target energy column
feature_cols = [col for col in ["temp", "humidity", "wind_speed", "GHI", "Hour", "Month"] if col in df.columns]
if not feature_cols:
    feature_cols = [c for c in df.select_dtypes(include=np.number).columns if "energy" not in c.lower()]

target_col = next(c for c in df.columns if any(k in c.lower() for k in ["energy", "output", "wh"]))

X = df[feature_cols]
y_reg = df[target_col]

# Binary classification target (1: High Output, 0: Low Output)
y_cls = (y_reg >= y_reg.median()).astype(int)

print("Features selected:", feature_cols)
print("Target column:", target_col)
