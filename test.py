import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from datetime import date,datetime
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
import numpy as np

try:
    df = pd.read_csv('record.csv')
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
    y_for_min = df['Minimum value']
    y_for_max = df['Maximum value']
    x_train, x_test, y_min, y_test = train_test_split(x, y_for_min, test_size=0.33, random_state=42)
    x_train, x_test, y_max, y_test = train_test_split(x, y_for_max, test_size=0.33, random_state=42)
    #RFR testing
    model_min = RandomForestRegressor(n_estimators=100)
    model_max = RandomForestRegressor(n_estimators=100)
    model_min.fit(x_train,y_min)
    model_max.fit(x_train,y_max)
    min_pred = model_min.predict(x_test)
    max_pred = model_max.predict(x_test)
    print(mean_absolute_error(y_test,max_pred))
    print(mean_absolute_error(y_test,min_pred))
    print(model_min.score(x_test, y_test))
    print(model_max.score(x_test, y_test))
    #Convert commodity into original values
    x_test_origin = le.inverse_transform(x_test['Commodity'])
    print("Minimum  :")
    for com,pre in zip(x_test_origin[:5],min_pred[:5]):
        
        print(com,pre)
    print("Maximum  :")
    for com,pre in zip(x_test_origin[:5],max_pred[:5]):
        
        print(com,pre)
    print(df['Commodity'].nunique())
    print(Dates.min(), Dates.max())    
    print(len(df))
    

except FileNotFoundError:
    print("Error")

