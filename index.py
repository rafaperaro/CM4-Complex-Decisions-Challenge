import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
import seaborn as sns

# Imports Puapa New Guinea Weather Data and safes it as a Dataframe

df = pd.read_csv('./data/Papua New Guinea Weather Data 2022.csv')

# Drops Rows that are not part of the analysis

df = df.drop(columns=['name', 'stations', 'uvindex', 'visibility', 'sealevelpressure', 'winddir', 'windspeed', 'windgust', 'preciptype', 'snowdepth', 'snow', 'precipprob', 'precip', 'dew', 'humidity', 'feelslike', 'feelslikemax', 'feelslikemin', 'severerisk'], axis=1)

# Creates column hoursofsunlight that stores the hours between sunrise and sunset rounded to the hour

hours_of_sunlight = []
date_format = '%Y-%m-%dT%H:%M:%S'

for sunrise, sunset in zip(df['sunrise'], df['sunset']):
    sr = datetime.strptime(sunrise, date_format)
    ss = datetime.strptime(sunset, date_format)
    hours = (ss -sr).total_seconds() / 3600
    hours_of_sunlight.append(hours)

df['hoursofsunlight'] = hours_of_sunlight

#Creates a column totalsolarradiation which stores the watts per square meter for each day of the year

df['totalsolarradiation'] = df['hoursofsunlight'] * df['solarradiation']

# Plots histogram of totalsolarradiation
sns.set_style("whitegrid")

plt.hist(df['totalsolarradiation'], bins=12, color='#C9D4E7', align='mid', edgecolor='#4878CF', linewidth=2)
plt.title('Total Radiation per day (W/m²)', fontweight='bold')
plt.xlabel('Radiation per day (W/m²)')
plt.ylabel('Frequency')
plt.show()

# Plots a line graph of totalsolarradiation for each year
