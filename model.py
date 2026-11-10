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

y_cls = (y_reg >= y_reg.median()).astype(int)

print("Features selected:", feature_cols)
print("Target column:", target_col)


# data splitting and normalization(80% train 20% test split)
# 80% train, 20% test split
X_train, X_test, y_train_reg, y_test_reg, y_train_cls, y_test_cls = train_test_split(
    X, y_reg, y_cls, test_size=0.2, random_state=42
)
scaler = StandardScaler() #feature scaling
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

print(f"Train size: {len(X_train)} | Test size: {len(X_test)}")

# Model Training
def train_regressor(X_tr, y_tr):
    model = LinearRegression()
    model.fit(X_tr, y_tr)
    return model

def train_classifier(X_tr, y_tr):
    model = LogisticRegression()
    model.fit(X_tr, y_tr)
    return model

reg_model = train_regressor(X_train_scaled, y_train_reg)
cls_model = train_classifier(X_train_scaled, y_train_cls)

def evaluate_regressor(model, X_te, y_te):
    y_pred = model.predict(X_te)
    rmse = np.sqrt(mean_squared_error(y_te, y_pred))
    mae = mean_absolute_error(y_te, y_pred)
    r2 = r2_score(y_te, y_pred)
    print(f"\n[Regression] R2: {r2:.3f} | RMSE: {rmse:.3f} | MAE: {mae:.3f}")
    return y_pred

def evaluate_classifier(model, X_te, y_te):
    y_pred = model.predict(X_te)
    acc = accuracy_score(y_te, y_pred)
    prec = precision_score(y_te, y_pred, zero_division=0)
    rec = recall_score(y_te, y_pred, zero_division=0)
    f1 = f1_score(y_te, y_pred, zero_division=0)
    cm = confusion_matrix(y_te, y_pred)
    print(f"[Classification] Acc: {acc:.3f} | Prec: {prec:.3f} | Rec: {rec:.3f} | F1: {f1:.3f}")
    return y_pred, cm

reg_preds = evaluate_regressor(reg_model, X_test_scaled, y_test_reg)
cls_preds, cm = evaluate_classifier(cls_model, X_test_scaled, y_test_cls)
