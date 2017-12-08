#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 15 10:37:54 2017

@author: Dan
"""
import pandas as pd
import requests
import datetime
from bs4 import BeautifulSoup



headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36'
            }
url = 'https://www.investing.com/indices/hang-seng-china-enterprises-historical-data'
payload = {'Content-type':'application/x-www-form-urlencoded', 'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/603.3.8 (KHTML, like Gecko) Version/10.1.2 Safari/603.3.8', 'Referer':'https://www.investing.com/indices/hang-seng-china-enterprises-historical-data' }
rs = requests.get( url, headers = headers, data = payload).text

soup = BeautifulSoup(rs, 'lxml')
a = soup.find('span' ,{'id':'last_last'})

value = float(str(a).split('>')[1].split('<')[0].replace(',',''))
date = datetime.datetime.now().strftime('%Y-%m-%d')
print(value, date)

#Save.Save_Single_Value(slug='china-hang-seng-china-enterprise',date=date,value=value)