#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 21 17:00:53 2017

@author: Dan
"""

# Data cleaning
#爬蟲
import pandas as pd 

stockcodeurl = 'http://isin.twse.com.tw/isin/C_public.jsp?strMode=2'
rawdata = pd.read_html(stockcodeurl)[0]

#整理股票代碼及名稱
stockcode=[]
stockname=[]

for i in range(2, 902, 1):
    try:
        raw = rawdata.iloc[i,0].split('\u3000')
        #print(raw)
    
        stockcode.append(rawdata.iloc[i,0].split('\u3000')[0])
        stockname.append(rawdata.iloc[i,0].split('\u3000')[1])
    except:
        stockname.append('全宇生技-KY')

stockcode[651] = str.split('4148 全宇生技-KY')[0]

#整理上市日期(證交所資料從民國81年開始)

start = rawdata.iloc[2:902, 2]
yearstart =[]
monthstart =[]

for i in range(2, 902, 1):
    year = start[i].split('/')[0]
    month = start[i].split('/')[1]
    yearstart.append(year)
    monthstart.append(month)
    
newyearstart = []
newmonthstart = []

for i in range( 0, len(yearstart), 1):
    a = int(yearstart[i])
    if a <= 1992 :
        newyearstart.append(1992)
        newmonthstart.append('01')
    else:
        newyearstart.append(a)
        newmonthstart.append(monthstart[i])


#Data processing

#1 上市日期分類： a. 1992年以前就上市 b. 1992年以後才上市
#2 1992年以前上市：
#   step1 先把資料抓到今年以前
#   step2 在抓當年度資料
#3 1992年以後上市：
#   step1 先抓上是當年資料
#   step2 抓今年以前的資料
#   step3 抓當年度資料


import datetime

urllist =[]
month = ['01','02','03','04','05','06','07','08','09','10','11','12']

thisyear = 2017
thismonth = int(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S").split(' ')[0].split('-')[1])

#getdata('2330')
def getdata(id):
    position = stockcode.index(id)
    tmp0 = newmonthstart[position]
    tmp1 = newyearstart[position]
    if tmp0 == '01' and tmp1 == 1992 :
        for y in range(tmp1, thisyear, 1):
            for m1 in range(0, len(month), 1):
                url = 'http://www.twse.com.tw/exchangeReport/STOCK_DAY?response=html&date='+ str(y) + str(month[m1]) + '01' + '&stockNo=' + id
                urllist.append(url)
        for m2 in range(0, thismonth, 1):
            url2 = 'http://www.twse.com.tw/exchangeReport/STOCK_DAY?response=html&date='+ str(thisyear) + str(month[m2]) + '01' + '&stockNo=' + id
            urllist.append(url2)
            
        date = []
        volumn=[]
        op = []
        close = []
        high = []
        low =[]
        
        for l in range(0, len(urllist),1):
                df = pd.read_html(urllist[l])[0]
                for k in range(0, len(df.index),1):
                    time = df.iloc[k,0]
                    time = str(int(time.split('/')[0])+1911) + '-'+ time.split('/')[1] +'-'+ time.split('/')[2]
                    date.append(time)
                    volumn.append(df.iloc[k,1])
                    op.append(df.iloc[k,3])
                    high.append(df.iloc[k,4])
                    low.append(df.iloc[k,5])
                    close.append(df.iloc[k,6])
        id = pd.DataFrame({'open':op,'close':close, 'high':high, 'low':low, 'volumn':volumn}, index= date)
        print(id)
        return(id)
    
    else:
        for m1 in range(int(tmp0)-1, 12, 1):
            url = 'http://www.twse.com.tw/exchangeReport/STOCK_DAY?response=html&date='+ str(tmp1) + str(month[m1]) + '01' + '&stockNo=' + id
            urllist.append(url)
        for y in range(tmp1+1, thisyear, 1):
            for m2 in range(0, len(month), 1):
                url2 = 'http://www.twse.com.tw/exchangeReport/STOCK_DAY?response=html&date='+ str(y) + str(month[m2]) + '01' + '&stockNo=' + id
                urllist.append(url2)
        for m3 in range(0, thismonth, 1):
            url3 = 'http://www.twse.com.tw/exchangeReport/STOCK_DAY?response=html&date='+ str(thisyear) + str(month[m3]) + '01' + '&stockNo=' + id
            urllist.append(url3)
            
        date = []
        volumn=[]
        op = []
        close = []
        high = []
        low =[]
        
        for l in range(0, len(urllist),1):
            df = pd.read_html(urllist[l])[0]
            for k in range(0, len(df.index),1):
                time = df.iloc[k,0]
                time = str(int(time.split('/')[0])+1911) + '-'+ time.split('/')[1] +'-'+ time.split('/')[2]
                date.append(time)
                volumn.append(df.iloc[k,1])
                op.append(df.iloc[k,3])
                high.append(df.iloc[k,4])
                low.append(df.iloc[k,5])
                close.append(df.iloc[k,6])
        id = pd.DataFrame({'open':op,'close':close, 'high':high, 'low':low, 'volumn':volumn}, index= date)
        print(id)
        return(id)


#function輸入 getdata2(id, yyyy, m, yyyy, m), eg. getdata2('1101', 2010, 1, 2013, 5)

def getdata2(id, by, bm, ey, em):
    position = stockcode.index(id)
    tmp0 = newmonthstart[position]
    tmp1 = newyearstart[position]
    if int(by) < tmp1 :
        print('輸入時間超過資料範圍')
    elif int(by) == tmp1 and int(bm) < int(tmp0):
        print('輸入時間超過資料範圍')
    elif int(ey) > thisyear:
        print('輸入時間超過資料範圍')
    elif int(ey) == thisyear and int(em) > thismonth:
        print('輸入時間超過資料範圍')
    else:
        for m1 in range(int(bm)-1, 12, 1):
            url = 'http://www.twse.com.tw/exchangeReport/STOCK_DAY?response=html&date='+ str(by) + str(month[m1]) + '01' + '&stockNo=' + id
            urllist.append(url)
        for y in range(by+1, ey+1, 1):
            for m2 in range(0, len(month), 1):
                url2 = 'http://www.twse.com.tw/exchangeReport/STOCK_DAY?response=html&date='+ str(y) + str(month[m2]) + '01' + '&stockNo=' + id
                urllist.append(url2)
        for m3 in range(0, int(em), 1):
            url3 = 'http://www.twse.com.tw/exchangeReport/STOCK_DAY?response=html&date='+ str(ey) + str(month[m3]) + '01' + '&stockNo=' + id
            urllist.append(url3)
            
        date = []
        volumn=[]
        op = []
        close = []
        high = []
        low =[]
        
        for l in range(0, len(urllist),1):
            df = pd.read_html(urllist[l])[0]
            for k in range(0, len(df.index),1):
                time = df.iloc[k,0]
                time = str(int(time.split('/')[0])+1911) + '-'+ time.split('/')[1] +'-'+ time.split('/')[2]
                date.append(time)
                volumn.append(df.iloc[k,1])
                op.append(df.iloc[k,3])
                high.append(df.iloc[k,4])
                low.append(df.iloc[k,5])
                close.append(df.iloc[k,6])
        id = pd.DataFrame({id : close}, index= date)
        return(id)
        
    
getdata('2330')