# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.


with open('%s.txt' % curr_name) as infile, open('%s.csv' % curr_name,'w') as outfile: 
                    for line in infile: 
                        
                        outfile.write(line)

"""
#RUN ONCE AT BEGINNING, NEVR TOUCH AGAIN

import os,csv
import pdb
import pandas as pd
from operator import itemgetter
import numpy as np
curr_dir='.'
firstline=1
title=""
summary=""
data=[]
readable=[]
Final=[]
softwareBug=[]
hardwareBug=[]
humanError=[]
networkBug=[]
undeterminedBug=[]
facilityBug=[]
final=[]
integer=0
fileCounter=1


for file in os.listdir(curr_dir):
    if ".txt" not in file or "node" in file or "data" not in file or "node" in file:
        continue
    with open (file, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=",")
        for line in enumerate(reader):
            
            if firstline==2:
                summary=line[1]
                firstline=3
                continue
                
            if firstline==1:
                title=line[1][0]
                firstline=2
                continue
            
            data.append([cWord for cWord in line[1]])
            tester=0 
            
    #sort method for list based on timestamp
    #sort by cluster as well
    #what parameters to order data?
    #separate based on sys num
    
    for vector in data:
        currTimeList=vector[16].split()
        currDate=currTimeList[0].split('/')
        currDateTime=float(currDate[0])*30+float(currDate[1])+float(currDate[2])*365
        currHour=currTimeList[1].split(':')
        Time=(((float(currHour[0])+float(currHour[1])/60)/24)+currDateTime)
        vector[16]=float(Time)/(24*60)
        #minutes
        
    data.sort(key=lambda x:x[16])
    minele=data[0][16]
    maxele=data[len(data)-1][16]-minele
    
    for vector in data:
        vector[16]=vector[16]-minele 
        
    data.sort(key=lambda x:x[0])
    current_number=data[0][0]
    old_index=0
    new_index=1
    for integer in range(len(data)):
        if data[integer][0] != current_number:
            curr_name="Node "+str(current_number)+" in file "+file
            f=open('%s.txt' % curr_name, 'w+')
            f.write("Type,Time")
            f.write("\n")
            
            for row in range(old_index, new_index-1):
                cstr=""
                for column in range (19,25):
                    if data[row][column] != "":
                        if column==19:
                            cstr="Facility Error,"
                        if column==20:
                            cstr="Hardware Error,"
                        if column==21:
                            cstr="Human Error,"
                        if column==22:
                            cstr="Network Error,"
                        if column==23:
                            cstr="Undetermined Error,"
                        if column==24:
                            cstr="Software Error,"
                if cstr=="":
                    continue
                
                cstr+=str(data[row][16])          
                f.write(cstr)
                f.write("\n")
            c_name=curr_name+".txt"
            f=open(c_name,'r')
            curr_name=curr_name+".csv"
            csvfile=open(curr_name,'w+')
            for line in f:
                csvfile.write(line)
            old_index=new_index+1
            new_index=new_index+1
            current_number=data[integer][0]
        else :
            new_index=new_index+1



    