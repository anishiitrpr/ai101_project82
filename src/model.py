import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.metrics import mean_squared_error, r2_score, accuracy_score

print("Running model.py...")

# 1. Load the cleaned dataset
df = pd.read_csv("data/cleaned_data.csv")

# 2. Select features and target variables
# Hardcoding the weather columns we want to use for predictions
X = df[['temp', 'humidity', 'wind_speed', 'GHI']]

# Target for Linear Regression (continuous values)
y_continuous = df['Energy delta[Wh]']

# Target for Logistic Regression (0 for no energy, 1 for energy produced)
# This simple logic fixes the 1-class ValueError
df['energy_class'] = 0
df.loc[df['Energy delta[Wh]'] > 0, 'energy_class'] = 1
y_categorical = df['energy_class']

# 3. Split the data into 80% training and 20% testing
X_train, X_test, y_train_reg, y_test_reg = train_test_split(X, y_continuous, test_size=0.2, random_state=42)
# We can use the same X split for classification
_, _, y_train_cls, y_test_cls = train_test_split(X, y_categorical, test_size=0.2, random_state=42)

# 4. Scale the data so all features have equal weight
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 5. Train Linear Regression Model
print("\n--- Training Linear Regression ---")
lin_model = LinearRegression()
lin_model.fit(X_train_scaled, y_train_reg)

reg_predictions = lin_model.predict(X_test_scaled)

# Calculate and print metrics
r2 = r2_score(y_test_reg, reg_predictions)
rmse = np.sqrt(mean_squared_error(y_test_reg, reg_predictions))

print("Linear Regression R2 Score:", round(r2, 3))
print("Linear Regression RMSE:", round(rmse, 3))

# 6. Train Logistic Regression Model
print("\n--- Training Logistic Regression ---")
log_model = LogisticRegression()
log_model.fit(X_train_scaled, y_train_cls)

cls_predictions = log_model.predict(X_test_scaled)

# Calculate and print accuracy
accuracy = accuracy_score(y_test_cls, cls_predictions)
print("Logistic Regression Accuracy:", round(accuracy, 3))

print("\nModel training completed successfully!")
