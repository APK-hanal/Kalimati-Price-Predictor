import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from datetime import date,datetime
from sklearn.preprocessing import LabelEncoder
import numpy as np

try:
    f = pd.read_csv('record.csv')
    print("Yeehaw")
    df = pd.DataFrame(f)
    Dates = pd.to_datetime(df['Date'])
    Year = Dates.dt.year
    Month = Dates.dt.month
    Day = Dates.dt.day
    df['Year'] = Year
    df['Month']= Month
    df['Day'] = Day
    commodity = df['Commodity']
    Mins = df['Minimum value']
    Maxs = df['Maximum value']
    avgs = df['Average']
    df.drop('Date', axis=1, inplace=True)
    le = LabelEncoder()
    df['Commodity'] = le.fit_transform(df['Commodity'])
    print(df['Commodity'])
except FileNotFoundError:
    print("Error")

