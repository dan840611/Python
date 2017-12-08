#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 15:54:57 2017

@author: Dan
"""

import pandas as pd
import requests
import json
import datetime as dt
import Save_to_SQL as Save

def get_investing(url):
    headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36'
            }
    
    rs = requests.get(str(url), headers = headers).text
    data = json.loads(rs)
    #print (data['data'])

    data = data['data']

    date = []
    value = []

    for i in range(0, len(data), 1):
        tmp1 = data[i][0]
        tmp2 = float(data[i][1])
        tmp1 = dt.datetime.fromtimestamp(tmp1/1000) #- dt.timedelta(days = 20)
        date.append(tmp1.strftime('%Y-%m-%d')) #   -01
        value.append(tmp2)
    
    #記得改名字
    df = pd.DataFrame({'india-interest-rate':value, 'date':date}, index= date)
    data = df.drop_duplicates(subset = 'date', keep = 'last').drop('date', axis = 1)
    print(data)
  
# india interest rate
url = 'https://sbcharts.investing.com/events_charts/us/597.json'
get_investing(url)
#Save.Save_SeriesData(slug = '', Series = data['india-basic-interest-rate'])


################################################################################################################

import pandas as pd
import requests
import json
import datetime as dt
import Save_to_SQL as Save


def get_investing(url):
    headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36'
            }
    
    rs = requests.get(str(url), headers = headers).text
    data = json.loads(rs)
    #print (data['data'])

    data = data['data']

    date = []
    value = []

    for i in range(0, len(data), 1):
        tmp1 = data[i][0]
        tmp2 = float(data[i][1])
        tmp1 = (dt.datetime.fromtimestamp(tmp1/1000) - dt.timedelta(days = 50))
        date.append(tmp1.strftime('%Y-%m-01')) #   -01
        value.append(tmp2)
    
    #記得改名字
    df = pd.DataFrame({'india-IIP-yoy':value, 'date':date}, index= date)
    data = df.drop_duplicates(subset = 'date', keep = 'last').drop('date', axis = 1)
    print(data)


# india index of industrial production
url = 'https://sbcharts.investing.com/events_charts/us/435.json'
get_investing(url)

#Save.Save_SeriesData(slug = 'india-industries-index-production', Series = data['india-IIP-yoy'])
