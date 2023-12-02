import pandas as pd

# Imports Puapa New Guinea Weather Data and safes it as a Dataframe
df = pd.read_csv('./data/Papua New Guinea Weather Data 2022.csv')

# Drops Rows that are not part of the analysis
df = df.drop(columns=['name', 'stations', 'uvindex', 'visibility', 'sealevelpressure', 'winddir', 'windspeed', 'windgust', 'preciptype', 'snowdepth', 'snow', 'precipprob', 'precip', 'dew', 'humidity', 'feelslike', 'feelslikemax', 'feelslikemin', 'severerisk'], axis=1)

# Creates Collumn hoursofsunlight that stores the hours between sunrise and sunset rounded to the hour

hoursofsunlight = []

for sunrise, sunset in zip(df['sunrise'], df['sunset']):
    print(sunrise)
    print(sunset)
