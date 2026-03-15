import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from datetime import date,datetime
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
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
    x = df[['Commodity', 'Year', 'Month', 'Day', 'Minimum value']]
    y = df['Maximum value']
    x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.33, random_state=42)
    model = RandomForestRegressor()
    model.fit(x_train,y_train)
    
except FileNotFoundError:
    print("Error")

