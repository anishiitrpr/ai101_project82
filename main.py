import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#Load dataset
df=pd.read_csv("Renewable.csv")

#Display first 5 rows
print(df.head())

#Dataset information
print(df.info())

#Columns names 
print(df.columns)

#Dataset size
print(df.shape)

#Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

#Check duplicate records 
print("\nDuplicate Records:")
print(df.duplicated().sum())

#Statical analysis
print("\nStatistical Summary")
print(df.describe())

#Display all column names
print("\nColumn Names")
print(df.columns.tolist())

#Check data types
print("\nData Types")
print(df.dtypes)

#Check missing value in detail 
print("\nMissing Value")
print(df.isnull().sum().to_string())

#Display first 10 records 
print("\nFirst 10 Records")
print(df.head(10))

#Missing values is zero in every column so we do not need to fill missing values

#Check duplicate records 
print("\nDuplicate Records")
print(df.duplicated().sum())

#Remove duplicate records

df=df.drop_duplicates()
print("\nDataset after removing duplicates:")
print(df.shape)

#Convert Time column into datetime 
df['Time']=pd.to_datetime(df['Time'])

#Sort dataset according to time
df=df.sort_values(by='Time')
print("\nTime column converted successfully")
print(df['Time'].dtype)

#Final dataset information 
print("\nFinal Dataset information:")
print(df.info())
print("\nFinal Dataset:")
print(df.head())

#Save cleaned dataset 
df.to_csv("cleaned_data.csv",index=False)
print("\nCleaned dataset saves susccesfully !")
print("Final dataset shape",df.shape)

#Verify cleaned dataset 
print("\nMissing values after cleaning")
print(df.isnull().sum())
print("\nDuplicate records after cleaning ")
print(df.duplicated().sum())
print("\nFinal columns :")
print(df.columns.tolist())
print("\nFinal data shape:")
print(df.shape)

#  dataset structure for ml

print("\n==================DATASET STRUCTURE" \
"===========")

#display all column names 
print("\nAvailable Columns :")
print(df.columns.tolist())

#display data types
print("\nColumn Data types :")
print(df.dtypes)

#display first 10 records 
print("\nDataset preivew:")
print(df.head(10))

#display numeric columns 
print("\nNumerical columns ")
print(df.select_dtypes(include=np.number).columns.tolist())

#display categorical columns 
print("\nCategorical Columns:")
print(df.select_dtypes(include='object').columns.tolist())

# feature engineering 

#extract date and time features 
if'Time'in df.columns:

    df['Year']=df["Time"].dt.year
    df['Month']=df["Time"].dt.month
    df['Day']=df["Time"].dt.day
    df['Hour']=df["Time"].dt.hour

    print("\nTime feature created successfully")



#display updated dataset
print("\nupdated dataset:")
print(df.head())

print("\nupdated dataset shape:")
print(df.shape)


# Save featured engineered dataset
df.to_csv("feature_engineered_data.csv",index=False)

print("\nFeature engineered dataset savd successfully")
print("final shape",df.shape)

# Final dataset validation

import os
import pandas as pd

file_name = "cleaned_data.csv"

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
