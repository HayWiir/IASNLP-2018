#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  6 08:24:52 2018

@author: rishav
"""
def intersection(lst1, lst2):
    return list(set(lst1) & set(lst2))

totalPrecision=0
totalRecall=0
lower=1
limit=31
for i in range(lower,limit):
    #print("File No:"+str(i))
    file=open("Actual Log Files/ALog-"+str(i)+".txt",'r')
    actualTxt=file.read()
    file2=open("Rule Based Log Files/Log-"+str(i)+".txt",'r')
    predictedTxt=file2.read()
    actualList=actualTxt.split("\n")
    predictedList=predictedTxt.split("\n")
       
    del actualList[len(actualList)-1]
    del predictedList[len(predictedList)-1]
   
    for dex in range(len(actualList)):
        actualList[dex]=actualList[dex].strip()
    for dex in range(len(predictedList)):
        predictedList[dex]=predictedList[dex].strip()
     
    res=intersection(actualList,predictedList)
    #print(res)
    if(len(predictedList)==0 and len(actualList)==0):
        res.append(0)
    if(len(predictedList) == 0 ):
        predictedList.append(0)
    if(len(actualList) == 0):
        actualList.append(0)
    
    precisionPerFile=len(res)/len(predictedList)
    recallPerFile=len(res)/len(actualList)
    #print("P: "+ str(precisionPerFile))
    #print("R: "+ str(recallPerFile))
    if(recallPerFile < 1.0):
        print(str(i)+" "+ str(recallPerFile))
    totalPrecision+=precisionPerFile
    totalRecall+=recallPerFile

meanPrecision=totalPrecision/(limit-lower)
meanRecall=totalRecall/(limit-lower)
print("Mean Recall:"+str(meanRecall))
print("Mean Precision:"+str(meanPrecision))

    