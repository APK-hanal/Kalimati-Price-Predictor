import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from datetime import date,datetime
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
import numpy as np

try:
    f = pd.read_csv('record.csv')
    print("Yeehaw")
    
    df = pd.DataFrame(f)
    Dates = pd.to_datetime(df['Date'])
    #Time conversion
    Year = Dates.dt.year
    Month = Dates.dt.month
    Day = Dates.dt.day
    df['Year'] = Year
    df['Month']= Month
    df['Day'] = Day
    print(df['Average'].dtype)
    commodity = df['Commodity']
    Mins = df['Minimum value']
    Maxs = df['Maximum value']
    avgs = df['Average']
    
    df.drop('Date', axis=1, inplace=True)
    le = LabelEncoder()
    df['Commodity'] = le.fit_transform(df['Commodity'])
    x = df[['Commodity', 'Year', 'Month', 'Day']]   
    y = df['Average']
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.33, random_state=42)
    #RFR testing
    model = RandomForestRegressor(n_estimators=100)
    model.fit(x_train,y_train)
    y_pred = model.predict(x_test)
    print(mean_absolute_error(y_test,y_pred))
    print(model.score(x_test, y_test))
    #Convert commodity into original values
    x_test_origin = le.inverse_transform(x_test['Commodity'])
    for com,pre in zip(x_test_origin[:5],y_pred[:5]):
        print(com,pre)
    print(df['Commodity'].nunique())
    print(Dates.min(), Dates.max())    
    print(len(df))
    
    
    
except FileNotFoundError:
    print("Error")

