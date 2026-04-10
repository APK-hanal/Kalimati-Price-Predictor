import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from datetime import date,datetime
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import mean_absolute_error
import numpy as np

try:
    df = pd.read_csv('record.csv')
    df = df.sort_values('Date')
    print("Yeehaw")
    Dates = pd.to_datetime(df['Date'])
    #Time conversion
    Year = Dates.dt.year
    Month = Dates.dt.month
    Day = Dates.dt.day
    df['Year'] = Year
    df['Month']= Month
    df['Day'] = Day    
    df.drop('Date', axis=1, inplace=True)
    le = LabelEncoder()
    df['Commodity'] = le.fit_transform(df['Commodity'])
    x = df[['Commodity', 'Year', 'Month', 'Day']]   
    
    #Splitting the data
    y_for_min = df['Minimum value']
    y_for_max = df['Maximum value']
    split = int(len(df)*0.67)
    x_train = x.iloc[:split]
    x_test = x.iloc[split:]
    y_train_min = y_for_min.iloc[:split]
    y_test_min = y_for_min.iloc[split:]
    y_train_max = y_for_max.iloc[:split]
    y_test_max = y_for_max.iloc[split:]
    #RFR testing
    model_min = RandomForestRegressor(n_estimators=100)
    model_max = RandomForestRegressor(n_estimators=100)
    model_min.fit(x_train,y_train_min)
    model_max.fit(x_train,y_train_max)
    min_pred = model_min.predict(x_test)
    max_pred = model_max.predict(x_test)
    print(mean_absolute_error(y_test_min, min_pred))
    print(mean_absolute_error(y_test_max, max_pred))
    print(model_min.score(x_test, y_test_min))
    print(model_max.score(x_test, y_test_max))
    #Convert commodity into original values
    x_test_origin = le.inverse_transform(x_test['Commodity'])
    print("Minimum")
    for com,pre in zip(x_test_origin[:5],min_pred[:5]):  
        print(com,pre)
    print("Maximum  :")
    for com,pre in zip(x_test_origin[:5],max_pred[:5]):
        
        print(com,pre)
except FileNotFoundError:
    print("Error")

