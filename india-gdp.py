#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 14 12:06:20 2017

@author: Dan
"""


import pandas as pd
import requests
import json
import datetime




'''
# India real GDP growth rate
url = 'https://wows-api.wallstreetcn.com/v3/asset/snapshot/kline?fields=ceic_code,publish_at,real,predict&ceic_codes=211636502'

headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36'
        }

rs = requests.get(url, headers = headers).text
data = json.loads(rs)

data = data['data']['items']['211636502']

date = []
value = []


for i in range(0, len(data), 1):
    tmp1 = (dt.datetime.fromtimestamp(data[i][1]) - dt.timedelta(days = 50 )).strftime('%Y-%m-01')
    tmp2 = float(data[i][2])
    date.insert(0, tmp1)
    value.insert(0, tmp2)

date = pd.to_datetime(date)  
df = pd.DataFrame({'value':value}, index = date)
print(df)

    
#CPI（華爾街見聞怪怪的，所以改抓investing.com的）

url = 'https://sbcharts.investing.com/events_charts/us/973.json'

headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36'
        }

rs = requests.get(url, headers = headers).text
data = json.loads(rs)

data = data['data']

date = []
value = []


for i in range(0, len(data), 1):
    tmp1 = dt.datetime.fromtimestamp(data[i][0]/1000).strftime('%Y-%m-01')
    tmp2 = float(data[i][1])
    date.append(tmp1)
    value.append(tmp2)


date = pd.to_datetime(date)    
df = pd.DataFrame({'value':value}, index = date)
print(df)



#unemployment rate (yearly)

url = 'https://wows-api.wallstreetcn.com/v3/asset/snapshot/kline?fields=ceic_code,publish_at,real,predict&ceic_codes=355185137'

headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36'
        }

rs = requests.get(url, headers = headers).text
data = json.loads(rs)

data = data['data']['items']['355185137']

date = []
value = []


for i in range(0, len(data), 1):
    tmp1 = dt.datetime.fromtimestamp(data[i][1]).strftime('%Y-%m-01')
    tmp2 = data[i][2]
    date.insert(0, tmp1)
    value.insert(0, tmp2)
    
df = pd.DataFrame({'value':value}, index = date)
print(df)
'''

#trading economics, 2
url = ['https://tradingeconomics.com/india/gdp-constant-prices',
       'https://tradingeconomics.com/india/gross-fixed-capital-formation',
       'https://tradingeconomics.com/india/government-spending',
       'https://tradingeconomics.com/india/consumer-spending'
    ]


df = pd.read_html(url[1])[0]
df.columns = ['GDP-related', 'Last', 'Previous', 'Highest', 'Lowest', 'Unit', 'None']  
gdp_constant = float(df.iloc[3,1]) * 100
fixed_capital_formation = float(df.iloc[5,1]) * 100

df = pd.read_html(url[2])[0]
df.columns = ['GDP-related', 'Last', 'Previous', 'Highest', 'Lowest', 'Unit', 'None']
government = float(df.iloc[3,1]) * 100

df = pd.read_html(url[3])[0]
df.columns = ['GDP-related', 'Last', 'Previous', 'Highest', 'Lowest', 'Unit', 'None']
consumption = float(df.iloc[1,1]) * 100



Y = datetime.date.today().month - 3
Q = (((datetime.date.today().month - 3) % 12 or 12) - 1)//3 + 1

if Y <= 0 :
    year = (datetime.date.today().year -1 ).strftime('%Y')
else :
    year = datetime.date.today().strftime('%Y')

month = ['01', '04', '07', '10']

date = year + '-'  + month[Q-1] + '-' + '01'

#date = (datetime.datetime.today() - datetime.timedelta( days = 140)).strftime('%Y-%m-01')

print (date, gdp_constant, fixed_capital_formation, government, consumption)

#Save.Save_Single_Value(slug='india-gdp',date=date,value=gdp_constant)
#Save.Save_Single_Value(slug='india-capital-formation',date=date,value=fixed_capital_formation)
#Save.Save_Single_Value(slug='india-government-consumption',date=date,value=government)
#Save.Save_Single_Value(slug='india-private-consumption',date=date,value=consumption)








