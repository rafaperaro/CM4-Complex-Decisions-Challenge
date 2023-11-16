import pandas as pd

df = pd.read_csv('./data/Papua New Guinea Weather Data.csv')

print(df['solarenergy'].mean())
