#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 10 12:08:51 2017

@author: Dan
"""

import pandas as pd
import requests
import json
import datetime as dt

url = 'https://sbcharts.investing.com/events_charts/us/1316.json'

headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36'
        }

rs = requests.get(url, headers = headers).text
data = json.loads(rs)
#print (data['data'])

data = data['data']

date = []
value = []

for i in range(0, len(data), 1):
    tmp1 = data[i][0]
    tmp2 = float(data[i][1])
    tmp1 = (dt.datetime.fromtimestamp(tmp1/1000) - dt.timedelta(days = 20))
    date.append(tmp1.strftime('%Y-%m-01'))
    value.append(tmp2)

df = pd.DataFrame({'export-rate':value, 'date':date}, index= date)
data = df.drop_duplicates(subset = 'date', keep = 'last').drop('date', axis = 1)

