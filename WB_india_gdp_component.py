#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 11:52:32 2017

@author: Dan
"""

import chardet
import pandas as pd
#import requests

'''
#world bank 爬蟲 

#household final consumer consumption %GDP
url_c = 'http://api.worldbank.org/v2/en/indicator/NE.CON.PETC.ZS?downloadformat=csv'

#gross capital fromation %GDP
url_i = 'http://api.worldbank.org/v2/en/indicator/NE.GDI.TOTL.ZS?downloadformat=csv'

#government final consumption %GDP
url_g = 'http://api.worldbank.org/v2/en/indicator/NE.CON.GOVT.ZS?downloadformat=csv'

#import of goods and services %GDP
url_i = 'http://api.worldbank.org/v2/en/indicator/NE.IMP.GNFS.ZS?downloadformat=csv'

#export of goods and services %GDP
url_x = 'http://api.worldbank.org/v2/en/indicator/NE.EXP.GNFS.ZS?downloadformat=csv'


df = pd.read_csv(url_c,  errors='ignore')
print (df)
'''

India = ['india_consumption.csv','india_government.csv', 'india_investment.csv', 'india_import.csv', 'india_export.csv']

for i in range(0, len(India), 1):
    with open(India[i], 'rb') as f:
        result = chardet.detect(f.read())
        print(result)


data = pd.DataFrame()

for i in range(0, len(India), 1):
    tmp1 = pd.read_csv(India[i], encoding = 'UTF-8-SIG', skiprows = 111)
    tmp1 = tmp1.iloc[ 0, 4:]
    tmp1 = pd.Series.to_frame(tmp1)
    tmp1.colunms = [India[i].split('.')[0]]
    data = pd.concat([data, tmp1], axis = 1)



#創造日期
I =[]

for j in range(0, len(data), 1):
    a = str(int(str.split(data.index[j])[1]) + 1956) + '-01-01'
    I.append(a)


data.index = I
data = data.dropna()
data.index = pd.to_datetime(data.index)
data.columns = India
print(data)


#
df1 = pd.DataFrame({'india-consumption' : data[India[0]]}, index = data.index)
df2 = pd.DataFrame({'india-government' : data[India[1]]}, index = data.index)
df3 = pd.DataFrame({'india-investment' : data[India[2]]}, index = data.index)
df4 = pd.DataFrame({'india-import' : data[India[3]]}, index = data.index)
df5 = pd.DataFrame({'india-export' : data[India[4]]}, index = data.index)




'''
with open('API_NE.CON.PETC.ZS_DS2_en_csv_v2.csv', 'rb') as f:
    result = chardet.detect(f.read())
    print (result)
    
df_c = pd.read_csv('API_NE.CON.PETC.ZS_DS2_en_csv_v2.csv', encoding = 'UTF-8-SIG', skiprows = 111)

print(df_c)



india_c = df_c.iloc[0,4:]
india_c = pd.Series.to_frame(india_c)
india_c.columns =['India_c']

I =[]


for i in range(0, len(india_c), 1):
    a = str(int(str.split(india_c.index[i])[1]) + 1956) + '-01-01'
    I.append(a)


india_c.index = I
india_c = india_c.dropna()
india_c.index = pd.to_datetime(india_c.index)

print(india_c)
'''