# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 07:02:14 2019

@author: anish
"""

"""
Change the ARIMA order for fine tuning
current best 2 1 0
4 0 3 v slow
"""
import csv
from pandas import datetime
import pandas as pd
from matplotlib import pyplot
from statsmodels.tsa.arima_model import ARIMA
from sklearn.metrics import mean_squared_error
from math import sqrt
incorrect=0
correct=0
series = pd.read_csv('test.csv', header=0, parse_dates=[0], index_col=0, squeeze=True)
# split into train and test sets
X = series.values
size = int(len(X) * 0.66)
train, test = X[0:size], X[size:len(X)]
history = [x for x in train]
predictions = list()
predictedBuffer=[]
for t in range(len(test)):
    model = ARIMA(history, order=(2,1,0))
    model_fit = model.fit(disp=0)
    output = model_fit.forecast()
    yhat = output[0]
    predictions.append(yhat)
    obs = test[t]
    history.append(obs)
    predictedBuffer.append((yhat,obs))
    print('predicted=%f, expected=%f' % (yhat, obs))
error = mean_squared_error(test, predictions)
print('Test MSE: %.3f' % error)
# plot
#print('incorrect: %f/%f' %(incorrect,correct))
pyplot.plot(test)
pyplot.plot(predictions, color='red')
pyplot.show()
incorrect=0
for tup in predictedBuffer:
    if tup[0][0]>.45: 
        tup[0][0]=1
    else:
        tup[0][0]=0
    if tup[0][0]!=tup[1]:
        incorrect+=1
        
print(incorrect)
        