# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import os,csv
from operator import itemgetter
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
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
integer=0
fileCounter=1
for file in os.listdir(curr_dir):
    if ".txt" not in file or "Output" in file:
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
    TIMES=[]
    for vector in data:
        currTimeList=vector[16].split()
        currDate=currTimeList[0].split('/')
        currDateTime=float(currDate[0])*30+float(currDate[1])+float(currDate[2])*365
        currHour=currTimeList[1].split(':')
        Time=(((float(currHour[0])+float(currHour[1])/60)/24)+currDateTime)
        TIMES.append(Time)
        vector[16]=float(Time)
    
    data.sort(key=lambda x:x[16])
    minele=data[0][16]
    maxele=data[len(data)-1][16]-minele
    for vector in data:
        vector[16]=vector[16]-minele 
    for vector in data:
        for integer in range(len(summary)):
            #tuples of error name, time, system
            if integer==0:
                integer=2
            if "Hard" in summary[integer] and vector[20]!="":
                hard_tuple=(vector[20], vector[16], vector[0])
                hardwareBug.append(hard_tuple)
                
            if "Human" in summary[integer] and vector[21]!="":
                human_tuple=(vector[21], vector[16], vector[0])
                humanError.append(human_tuple)
                
            if "Netw" in summary[integer] and vector[22]!="":
                net_tuple=(vector[22], vector[16], vector[0])
                networkBug.append(net_tuple)
                
            if "Undet" in summary[integer] and vector[23]!="":
                undet_tuple=(vector[23], vector[16], vector[0])
                undeterminedBug.append(undet_tuple)
                
            if "Soft" in summary[integer] and vector[24]!="":
                soft_tuple=(vector[24], vector[16], vector[0])
                softwareBug.append(soft_tuple)
                
            if "Faci" in summary[integer] and vector[19]!="":
                faci_tuple=(vector[19], vector[16], vector[0])
                facilityBug.append(faci_tuple)
doneErr=[]
totalCount=0
average=0
highest=0
top_freq=[]
error=""
hardwareBug=undeterminedBug

hardwareBug.sort(key=lambda x: x[2]) #now the current type of bug is sorted based on its system
currentNumber=hardwareBug[0][2]
mostPopErrors=[]
for integer in range(len(hardwareBug)):
        if currentNumber==hardwareBug[len(hardwareBug)-1][2]:
            currentNumber=-1
        if integer>len(hardwareBug):
            integer=0
        if currentNumber!=hardwareBug[integer][2]:
            currentBug=hardwareBug[0:integer]
            print ("This is the bug report for system #", hardwareBug[integer-1][2])
            for integer in range(len(currentBug)):
                currentCount=1
                freq=[]
                freq.append(currentBug[integer][1])
                if currentBug[integer][0] in doneErr:
                    continue
                for copynum in range(len(currentBug)):
                    if copynum==integer:
                        doneErr.append(currentBug[integer][0])
                        continue
                    
                    if currentBug[copynum][0]==currentBug[integer][0]:
                        currentCount+=1
                        freq.append(currentBug[copynum][1])
                    totalCount+=currentCount
                    average=((float(sum(freq))/365)/24)
    
    

#    if currentCount>=highest:
#        highest=currentCount
#        top_freq=freq
#        error=currentBug[integer][0]
                if (currentBug[integer][0]!=''):
                    print("")
                    print(currentBug[integer][0])
                    found=0;
                    for index, item in enumerate(mostPopErrors):
                        if item[0]==currentBug[integer][0]:
                            cnum=item[1]
                            cnum=cnum+1
                            item[1]=cnum
                            found=1
                    if found==0:
                        mostPopErrors.append((currentBug[integer][0], 1))
                    print(np.sum(freq))
                    num_bins=50
                    n,num_bins,patches=plt.hist(freq,num_bins, facecolor='blue', alpha=0.5)
                    plt.xlim(0,maxele)
                    plt.show()
            print("")
            print("")
            print("")
            hardwareBug=hardwareBug[-(len(hardwareBug)-integer):]
            currentNumber=hardwareBug[0][2]
            integer=1
for cTuple in mostPopErrors:
    print(cTuple[0], "  occured  ", cTuple[1], " times!")

    #date, when opening, when you start from timestamp, set that start to zero


#whole thing is sorted by system, and has a histogram of data








#with open("Output.txt", "w") as outputfile:
#    print("Hardware Bugs: {}\n".format(totalCount), file=outputfile)




