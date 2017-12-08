#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 10:16:26 2017

@author: Dan
"""

import datetime as datetime
import pandas as pd
import calendar
import requests
import json
import time

'''
##url
url = []
urllist = []


startyear = 2001
currentyear = int(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S").split(' ')[0].split('-')[0])


endmonth = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S").split(' ')[0].split('-')[1])

month = ['01','02','03','04','05','06','07','08','09','10','11','12']

# data prior to current year
for y in range(startyear, currentyear, 1):
    for m in range(0, len(month), 1):
        monthdays = calendar.monthrange(y,int(month[m]))[1]+1
        for d in range(1, monthdays, 1):
            if d < 10:
                d = '0' + str(d) 
                url = 'http://www.twse.com.tw/exchangeReport/MI_MARGN?response=json&date=' + str(y) + month[m] + d +  '&selectType=MS&_=1503281844590'
                urllist.append(url)
            else :
                url = 'http://www.twse.com.tw/exchangeReport/MI_MARGN?response=json&date=' + str(y) + month[m] + str(d) +  '&selectType=MS&_=1503281844590'
                urllist.append(url)

#current year
date1 = int(datetime.datetime.now().strftime('%Y-%m-%d').split('-')[2])
month1 = int(datetime.datetime.now().strftime('%Y-%m-%d').split('-')[1])
year1 = datetime.datetime.now().strftime('%Y-%m-%d').split('-')[0]

for m in range(1, month1, 1):
    monthdays = calendar.monthrange(y,int(month[m]))[1] + 1
    for d in range(1, monthdays, 1):
            if d < 10:
                d = '0' + str(d) 
                url = 'http://www.twse.com.tw/exchangeReport/MI_MARGN?response=json&date=' + year1 + month[m] + d +  '&selectType=MS&_=1503281844590'
                urllist.append(url)
            else :
                url = 'http://www.twse.com.tw/exchangeReport/MI_MARGN?response=json&date=' + year1 + month[m] + str(d) +  '&selectType=MS&_=1503281844590'
                urllist.append(url)
    
for d in range (1, date1, 1):
    if d < 10:
        d = '0' + str(d) 
        url = 'http://www.twse.com.tw/exchangeReport/MI_MARGN?response=json&date=' + year1 + month[m] + d +  '&selectType=MS&_=1503281844590'
        urllist.append(url)
    else :
        url = 'http://www.twse.com.tw/exchangeReport/MI_MARGN?response=json&date=' + year1 + month[m] + str(d) +  '&selectType=MS&_=1503281844590'
        urllist.append(url)

'''
##value
margintrading = []
shortselling = []
margintrading_m = []
date =[]

headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36'
        }

urllist1 = urllist[0:int(len(urllist)/6)]
urllist2 = urllist[int(len(urllist)/6):int(len(urllist)/3)]
urllist3 = urllist[int(len(urllist)/3):int(len(urllist)/2)]
urllist4 = urllist[int(len(urllist)/2):int((len(urllist)*2)/3)]
urllist5 = urllist[int((len(urllist)*2)/3):int((len(urllist)*5)/6)]
urllist6 = urllist[int((len(urllist)*5)/6):int(len(urllist))]


test = urllist[0:4]

def get(x):
    for i in range(0, len(x), 1):
        url = x[i]
        rs = requests.get(url, headers = headers).text
        data = json.loads(rs)
        
        tmp1 = pd.to_datetime(data['date']).strftime('%Y-%m-%d')
        date.append(tmp1)
                
        if len(data['creditList']) != 0 :
            margintrading.append(float(data['creditList'][0][5].replace(',','')))
            #shortselling.append(float(data['creditList'][1][5].replace(',','')))
            #margintrading_m.append(float(data['creditList'][2][5].replace(',','')))
                
        else:
            margintrading.append('NA')
            #shortselling.append('NA')
            #margintrading_m.append('NA')
                
        time.sleep(1)
        

    df1 = pd.DataFrame({'margintrading' : margintrading}, index =date)
    #df2 = pd.DataFrame({'shortselling': shortselling}, index =date)
    #df3 = pd.DataFrame({'margintrading_m' : margintrading_m}, index =date)
    #df = pd.concat([df1, df2, df3], axis = 1)
    #print (df)
    return df



df = pd.DataFrame()
for k in [urllist1, urllist2, urllist3, urllist4, urllist5, urllist6]:
    k = get(k)
    data = pd.concat([df, k], axis = 0)
    
#get('urllist1')
#get(urllist1)
