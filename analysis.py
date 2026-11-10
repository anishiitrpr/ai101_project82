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
print("/nDataset after removing duplicates:")
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
