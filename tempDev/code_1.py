import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.arima_model import ARIMA
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.tsa.stattools import adfuller
from sklearn.metrics import mean_squared_error

# Load your dataset (replace 'data.csv' with your dataset)
data = pd.read_csv('city.csv')
#print(data)
#print(data.isna().sum())
print(data.info())

# Replace missing values with the mean of the respective column
#data.fillna(data['2023-05-31'].mean(), inplace=True)

#missingData = data.isna().sum()
#print(missingData)

#print(data.info())
#print(data.describe())
            
# Take 
for column in data.columns:
    for row in range(len(data[column])):
        if data['RegionName'][row] == "New York":
            if column != 'RegionID' and column != 'RegionName' and  column != 'SizeRank' and column != 'RegionType' and column != 'StateName' and column != 'State' and column != 'Metro' and column != 'CountyName':
              print(data[column][row])
            
            





