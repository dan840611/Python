#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 17:49:04 2017

@author: Dan
"""

import pandas as pd

def read_mm(file):
    df = pd.read_csv(file,index_col=0, encoding = "ISO-8859-1")
    df.index = df.index.to_datetime()
    df['Value'] = df['Value'].astype('float')        
    return df

def read_mm2(file):
    df = pd.read_csv(file,index_col=0)
    df.index = df.index.to_datetime()
    df = df.applymap(lambda x: float(x.replace(",", "")))        
    return df


df1 = read_mm('3month_real.csv')
df2 = read_mm('sp500_yield.csv')
df3 = read_mm2('sp500.csv')

df = pd.concat([df1,df2,df3], axis=1) 
df = df.dropna()
df.columns =['real', 'yield', 'sp500'] 


df['after'] = df['yield'] - df['real']  
df = pd.concat([df['after'],df['sp500']], axis=1) 
df.to_csv('key.csv')