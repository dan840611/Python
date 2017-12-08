#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 23 11:00:10 2017

@author: Dan
"""
# Events
import pandas as pd
import numpy as np
import Fetch_MM_SQL as Fetch
import Save_to_SQL as Save
import datetime
#===================================================================================

#Monthly
Nonfarm = Fetch.Fetch_data2(44)[0]
#Daily
SP500 = Fetch.Fetch.data2(2)[0]

#設定條件
Nonfarm['signal'] = np.where(Nonfarm['44'] > 2000, 1,0)

# if Positive
Nonfarm['signal_1'] = np.where(Nonfarm['signal'].shift(1) < Nonfarm['signal'],1,0)


#和R語言相同 => 找出發生事件的日期
Date_list = Nonfarm[ Nonfarm['signal_1'] == 1 ].index

#====================================================================================

# -10未來十天的報酬率
SP500['Forward_Return'] = SP500['2'].pct_change(-10)
SP500 = SP500.dropna()
print(SP500)

#===================================================================================


#df= pd.DataFrame( index=pd.date_range('1950-01-01', datetime.datetime.today(), freqency= 'd')

df = SP500.resample('D', how='last')
df = df.fillna(method='ffill')


predict_table = pd.DataFrame()

for Date in Date_list:
        print (df[ df.index == Date])
        predict_table = pd.concat( [predict_table, df[ df.index == Date]] , axis=0)
        print (predict_table)


#計算勝率及平均報酬
predict_table['win-rate'] = np.where ( predict_table['Forward_Return'] >0 , 1, 0)

print (predict_table)

print (predict_table['Forward_Return'].mean())
print (predict_table['win-rate'].mean())