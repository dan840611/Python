# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 14:54:26 2017

@author: Yu-Lin
"""

import pandas as pd

# 如何將CSV檔讀寫進Python
def read_mm(file):
    df = pd.read_csv(file,index_col=0)
    df.index = df.index.to_datetime()
    df['Value'] = df['Value'].astype('float')        
    return df

df = read_mm('mm-twse.csv')
print (df)

#%% 基本DataFrame運算
import numpy as np

df.columns = ['twse']
df['MA5'] = df['twse'].rolling(window=5).mean()
df['MA20'] = df['twse'].rolling(window=20).mean()

#MA5是否大於MA20，顯示股價較為強勁
df['sign'] = np.where(df['MA5']>df['MA20'],1,0)

print (df)

#%% 基本Pandas 運用

# DataFrame如果為時間序列 可再重新整合頻率
data_monthly = df['twse'].resample('MS',how='mean')
data_weekly  = df['twse'].resample('W',how='last')
print (data_monthly ,data_monthly)

# DataFrame合併
df = pd.concat([data_monthly,data_weekly],axis=1)
print (df)

# 消除掉na值
df1 = df.dropna()
df2 = df.fillna(method='ffill')

print (df1 ,df2)

df1.plot()