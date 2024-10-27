import pandas as pd

df1 = pd.read_csv('fifa_teams_cleaned.csv')
print(df1.head())
print(df1.describe())
print(df1.info())

df2 = pd.read_csv('dz.csv')
print(df2.head())

group = df2.groupby('City')['Salary'].mean()
print(group)

