#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 18:21:33 2017

@author: Dan
"""
import pandas as pd
import requests
import json
import datetime as dt
#import Save_to_SQL as Save

def get_investing(url):
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
        tmp1 = dt.datetime.fromtimestamp(tmp1/1000) - dt.timedelta(days = 10)
        date.append(tmp1.strftime('%Y-%m-01')) #   -01
        value.append(tmp2)
    
    #記得改名字
    df = pd.DataFrame({'value':value}, index= date)
    print(df)
    return df
    
service = 'https://sbcharts.investing.com/events_charts/us/1477.json'
manufacture = 'https://sbcharts.investing.com/events_charts/us/1476.json'
composite = 'https://sbcharts.investing.com/events_charts/us/1475.json'


a = get_investing(manufacture)
#Save.Save_SeriesData(slug = 'brazil-manufacture-pmi', Series = a['value'])
b = get_investing(service)
#Save.Save_SeriesData(slug = 'brazil-service-pmi', Series = b['value'])
c = get_investing(composite)
#Save.Save_SeriesData(slug = 'brazil-pmi', Series = c['value'])