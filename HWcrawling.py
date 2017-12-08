#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 12 22:03:11 2017

@author: Dan
"""


year = ['2015','2016']
month = ['01','02','03','04','05','06','07','08','09','10','11','12']

urllist =[]


# for i in year
#    print(i)

def get_data(id):
    for i in range(0,len(year), 1):
        for m in range(0, len(month), 1):
            url = 'http://www.twse.com.tw/exchangeReport/STOCK_DAY?response=html&date='+ year[i] + str(month[m]) + '01' + '&stockNo=' + id
            urllist.append(url)
    
    date=[]
    value=[]
    
    import pandas as pd
    #import time
    
    for i in range(0, len(urllist),1):
        df = pd.read_html(urllist[i])[0]
        for k in range(0, len(df.index),1):
            time = df.ix[k,0]
            time = str(int(time.split('/')[0])+1911) + '-'+ time.split('/')[1] +'-'+ time.split('/')[2]
            date.append(time)
            value.append(df.ix[k,6])
        #time.sleep(1)
        
    df1 = pd.DataFrame({id:value}, index= date) 
    return df1  

df = get_data('2383')
print(df)



#Moving average
df["MA5"] = df["2383"].rolling(window=5).mean()
df["MA20"] = df["2383"].rolling(window=20).mean()
print(df)


#
import numpy as np

df["sign"] = np.where(df["MA5"] > df["MA20"],1,0)
print(df)

"""
#自定函數 sample
def Hello(name):
    print(name + "Hello")

Hello(name= "Gimmy")
"""

