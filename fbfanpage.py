#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 31 10:56:41 2017

@author: Dan
"""
import requests
import pandas as pd 
from dateutil.parser import parse
import json
import datetime as datetime

#取得FB API(定期更新) https://developers.facebook.com/tools/explorer/
token = 'EAACEdEose0cBANS2aapdz5Iul8911pjjjnW2dikZA0y9UR6EZBx03mXZCHEQ14z5xNJmHgYjF8zaVvsvFM0DOZAIaH1Dvv7OSo9Ma7ZBklWUU2j7UbYVr2tJyXdNK7kDDhnL2XDgZB3vFAa6NmZBCK1oWl18fZBGMWBjH8KvNDxoHsQZC2abFogQigrxytjjX84YZD'

fanpage ={
  "name": "MacroMicro 財經M平方",
  "id": "772440506218808",
  'post': '772440506218808_1309706875825499'
}


#/posts /comments 
url = 'https://graph.facebook.com/v2.9/{}/comments?limit=400&access_token={}'.format(fanpage['post'],token)

res = requests.get(url)
data = json.loads(res.text)
data = data['data']

time =[]
name =[]
message = []


for i in range(0, len(data), 1):
    tmp1 = datetime.datetime.strptime(data[i]['created_time'], '%Y-%m-%dT%H:%M:%S+0000') + datetime.timedelta(hours = 8)
    tmp2 = data[i]['from']['name']
    tmp3 = data[i]['message']
    time.append(tmp1)
    name.append(tmp2)
    message.append(tmp3)


df = pd.DataFrame()
df['time'] = time
df['name'] = name
df['message'] = message

#篩選留言時間
df1 = df[df['time'] < '2017-09-01 00:00:00']
#df2 = df1.drop_duplicates(subset = ['time'], keep = 'last')

#輸出excel
#df1.to_csv('lottery.csv', encoding = 'utf-8', index = False)
df.to_excel('lottery.xlsx', encoding = 'utf-8', index = False)
