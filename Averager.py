# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 05:06:32 2019

@author: anish
"""
'Shaping data to fit needs'
import pandas as pd
import os
import numpy as np
from sklearn.preprocessing import MinMaxScaler
import csv
TYPES=["1","2","3","4","5","6"]
chunk=1
def averager(data_type,time):
    start=0
    tiredOld=0
    tiredCurr=0
    one=[]
    two=[]
    three=[]
    four=[]
    five=[]
    six=[]
    
    for t in time:
        if t>(start+chunk):
            cArr=taker(data_type,tiredOld,tiredCurr)
            tiredOld=tiredCurr
            one.append((t,cArr.count(1)))
            two.append((t,cArr.count(2)))
            three.append((t,cArr.count(3)))
            four.append((t,cArr.count(4)))
            five.append((t,cArr.count(5)))
            six.append((t,cArr.count(6)))
            start=chunk
            #now we have array of all errors in current chunk sized interval
        tiredCurr=tiredCurr+1
    
    with open('test.csv', 'w') as f:
        writer = csv.writer(f , lineterminator='\n')
        for tup in three:
            writer.writerow(tup)
        
def taker(data_type,start,end):
    newArr=[]
    for x in range(start,end):
        newArr.append(data_type[x])
        print(newArr)
    return newArr
def read_Data():
    for file in os.listdir('.'):
        if "Node" not in file:
            continue
        
        df = pd.read_csv(file)
        data_type = df['Type']
        time=df['Time']
        #normalize to zero
        time[:]=[x-time[0] for x in time[:]]
        averager(data_type,time)
        #norm = [float(i)/max(time) for i in time]
        #time=norm
        #print(time)
#Regression not lSTM pls

    


#program starts
#os.remove('test.csv')
read_Data()
