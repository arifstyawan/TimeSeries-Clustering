import pandas as pd
import datetime
from datetime import date, timedelta
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.arima_model import ARIMA
from sklearn.metrics import mean_squared_error
from statsmodels.graphics.tsaplots import plot_pacf
import statsmodels.api as sm
from math import sqrt
import warnings
warnings.filterwarnings("ignore")

df = pd.read_csv('Case Study - Transaction.csv', sep=';')

df['Date'] = pd.to_datetime(df['Date'])
df = df.groupby('Date')['Qty'].sum().reset_index()
df.set_index('Date', inplace=True)

train, test = df.iloc[:335], df.iloc[335:]

model = sm.tsa.statespace.SARIMAX(train["Qty"],
                                  order=(5,1,1),
                                  seasonal_order=(5,1,1,30))
model = model.fit()
print(model.summary())

start = len(train)
end = len(train)+len(test)-1
predictions = model.predict(start=start, end=end)

rmse = sqrt(mean_squared_error(test["Qty"], predictions))
print('Test RMSE: %.3f' % rmse)

forecasting = model.predict(len(df), len(df)+30)
print(forecasting)

train["Qty"].plot(legend=True,
               label="Training Data",
               figsize=(9,5))
test["Qty"].plot(legend=True,
               label="Testing/Actual Data")
forecasting.plot(legend=True, label="Forecasting")