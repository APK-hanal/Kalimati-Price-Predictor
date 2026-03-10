import pandas as pd
from sklearn.linear_model import LinearRegression
from datetime import date,datetime
import numpy as np
try:
    f = pd.read_csv('record.csv')
    print("Yeehaw")
    df = pd.DataFrame(f)
    Dates = pd.to_datetime(df['Date'])
    Year = Dates.dt.year
    Month = Dates.dt.month
    Day = Dates.dt.day
    commodity = df['Commodity']
    Mins = df['Minimum value']
    Maxs = df['Maximum value']
    avgs = df['Average']
    print(Year,Month,Day)
except FileNotFoundError:
    print("Error")

