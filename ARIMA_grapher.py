# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 04:25:29 2019

@author: anish
"""
'Autoregressive integrated moving average'

from pandas import datetime
import pandas as pd
import csv
from matplotlib import pyplot
from statsmodels.tsa.arima_model import ARIMA
from sklearn.metrics import mean_squared_error
from math import sqrt
import pdb
series = pd.read_csv('test.csv', header=0, parse_dates=[0], index_col=0, squeeze=True)
# split into train and test sets

X = series.values
train, test = X[0:-250], X[-250:]
history = [x for x in train]
predictions = list()
# walk-forward validation
for t in range(len(test)):
	# fit model
	model = ARIMA(history, order=(4,1,0))
	model_fit = model.fit()
	# one step forecast
	yhat = model_fit.forecast()[0]
	# store forecast and ob
	predictions.append(yhat)
	history.append(test[t])
# evaluate forecasts
rmse = sqrt(mean_squared_error(test, predictions))
print('Test RMSE: %.3f' % rmse)
# plot forecasts against actual outcomes
#pyplot.plot(test)
pyplot.plot(test[0::10], label='Data')
pyplot.plot(predictions[0::10], color='red', label='Pred')
pyplot.show()