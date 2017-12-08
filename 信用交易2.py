#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 27 10:31:29 2017

@author: Dan
"""

import datetime as datetime
import pandas as pd
import requests
import json
import numpy as np
import time

'''
ty = datetime.datetime.now().strftime('%Y')
tm = datetime.datetime.now().strftime('%m')
td = datetime.datetime.now().strftime('%d').zfill(2)

yy = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime('%Y')
ym = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime('%m').zfill(2)
yd = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime('%d').zfill(2)
'''

today = datetime.datetime.today().strftime('%Y%m%d')
yesterday = (datetime.datetime.today() - datetime.timedelta(days = 1)).strftime('%Y%m%d')

def day(i):
    date = (datetime.datetime.today() - datetime.timedelta(days = i)).strftime('%Y%m%d')
    return(date)

url1 = 'http://www.twse.com.tw/exchangeReport/MI_MARGN?response=json&date=' + today +  '&selectType=MS&_=1503281844590'
url2 = 'http://www.twse.com.tw/exchangeReport/MI_MARGN?response=json&date=' + yesterday  +  '&selectType=MS&_=1503281844590'



def getcredit(url):
    headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36'
            }
    rs = requests.get(url, headers = headers).text
    data = json.loads(rs)
    
    tmp = url.split('=')[2].split('&')[0]
    date = pd.to_datetime(tmp[0:4] + tmp[4:6] + tmp[6:8])
    
    margintrading = []
    shortselling = []
    margintrading_m = []
    
    if len(data['creditList']) != 0 :
        margintrading = float(data['creditList'][0][5].replace(',',''))
        shortselling = float(data['creditList'][1][5].replace(',',''))
        margintrading_m = float(data['creditList'][2][5].replace(',',''))
    else :
        shortselling = np.nan
        margintrading_m = np.nan
        margintrading = np.nan
        
    ratio = []
    
    if margintrading_m == np.nan :
        ratio = np.nan
    else:
        ratio = float (shortselling / margintrading)
        #Save.Save_Single_Value(slug='taiwan-margin-trading',date=date,value=margintrading_m)
        #Save.Save_Single_Value(slug='taiwan-short-selling',date=date,value=shortselling)
        #Save.Save_Single_Value(slug='taiwan-short-selling-margin-trading-ratio',date=date,value=ratio)
        #Save.Save_Single_Value(slug='taiwan-margin-trading-unit',date=date,value=margintrading)
    print(shortselling, margintrading_m, margintrading, ratio, date)
    return (shortselling, margintrading_m, margintrading, ratio, date)


#抓近20天資料
"""
for i in range(0, 10, 1):
    day = (datetime.datetime.today() - datetime.timedelta(days = i)).strftime('%Y%m%d')
    url = 'http://www.twse.com.tw/exchangeReport/MI_MARGN?response=json&date=' + day +  '&selectType=MS&_=1503281844590'   
    print(url)
    getcredit(url)
    time.sleep(2)
"""

#找今天以前最近一次資料
for k in range(0, 20, 1):
    getcredit(url1)
    url = 'http://www.twse.com.tw/exchangeReport/MI_MARGN?response=json&date=' + day(k) +  '&selectType=MS&_=1503281844590'
    if np.isnan(getcredit(url)[0]):
        getcredit(url)
    else:
        break
    time.sleep(2)
