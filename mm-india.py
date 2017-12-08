#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 10:40:45 2017

@author: Dan
"""

import pandas as pd
import statsmodels.formula.api as smf

def read_mm(file):
    df = pd.read_csv(file,index_col=0, encoding = "ISO-8859-1")
    df.index = df.index.to_datetime()
    df['Value'] = df['Value'].astype('float')        
    return df

def read_mm2(file):
    df = pd.read_csv(file,index_col=0, encoding = "ISO-8859-1")
    df.index = df.index.to_datetime()
    for i in range(0, len(df)):
        df['Value'].iloc[i] = float(df['Value'].iloc[i].replace(',', ''))       
    return df

nas = read_mm2('/Users/Dan/Desktop/mm_nasdaq-composite.csv').resample('MS', how='last')
auto = read_mm2('/Users/Dan/Desktop/mm_us-auto-new-order.csv')
semi = read_mm2('/Users/Dan/Desktop/mm_tw-semi-billings.csv')
sensex = read_mm2('/Users/Dan/Desktop/sensex.csv').resample('MS', how='last')
df = pd.concat([nas, auto, semi, sensex], axis = 1)
df.columns = ['nas', 'auto', 'semi', 'sensex'] 
df['auto'] = df['auto'].shift(1)
df['semi'] = df['semi'].shift(1)
df = df.dropna()
df = (df - df.mean()) / df.std()

print(df)

#np.where(df.index == '2000-01-01')

df1 = df.iloc[:196 , :]
res = smf.ols(formula = 'sensex ~ nas + auto + semi', data = df1).fit()
print(res.summary())


