#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import statsmodels.api as sm

def read_mm(file):
    df = pd.read_csv(file,index_col=0, encoding = "ISO-8859-1")
    df.index = df.index.to_datetime()
    df['Value'] = df['Value'].astype('float')        
    return df

m1b = read_mm('/Users/Dan/Desktop/mm_tw-m1b-m2.csv') #3310
monitor = read_mm('/Users/Dan/Desktop/mm_tw-monitoring-indicators.csv') #390
electronic = read_mm('/Users/Dan/Desktop/mm_tw-export-electronic-yoy.csv') #511
twii = read_mm('/Users/Dan/Desktop/mm_tw-twii.csv')

m1b_shift = m1b.pct_change(12).dropna()
electronic = electronic.rolling(window=3).mean()
twii = twii.resample('MS', how= 'first')

cycle, trend = sm.tsa.filters.hpfilter(m1b_shift, 144000)
m1b_hp = trend

df = pd.concat([m1b_hp, electronic, monitor, twii], axis = 1)
df = df.dropna()
df.columns = ['m1b_hp', 'electronic', 'monitor', 'twii']

Index_df = (df - df.mean())/ (df.std())
Index_df.to_csv('/Users/Dan/Desktop/component.csv')
"""
Index_df['monitor'] = Index_df['monitor'] + 1
Index_df['MM'] = 0.35 * Index_df['m1b_hp'] + 0.55 * Index_df['monitor'] - 0.1 *Index_df['electronic']
print (Index_df)

Index_df.to_csv('/Users/Dan/Desktop/component.csv')
MM_index = Index_df.sum(axis = 1)*100.
MM_index.name = 'MM'


Date_shift = pd.concat([MM_index,twii],axis=1)
Date_shift = Date_shift['MM'].shift(3).dropna()
#Date_shift = Date_shift.rolling(window = 3). mean()
Date_shift = pd.concat([Date_shift,twii], axis=1)
Date_shift = Date_shift.dropna()

Date_shift.to_csv('/Users/Dan/Desktop/mm2.csv')
#Index_df.to_csv('/Users/Dan/Desktop/component.csv')
"""
'''
import matplotlib.pyplot as plt

fig = plt.figure()
ax1 = fig.add_subplot(111)
ax2 = ax1.twinx()

ax1.plot(Date_shift.index, Date_shift)
ax2.plot(twii.index, twii, 'R')
plt.show()


'''

'''
data_390 = Fetch.Fetch_data2(ID = 390)
data_369 = Fetch.Fetch_data2(ID = 369)
data_3310 = Fetch.Fetch_data2(ID = 3310)#3310
data_1360 = Fetch.Fetch_data2(ID = 1360)

TWSE = Fetch.Fetch_data2(ID = 693)[0].resample('MS',how='first')

df = pd.DataFrame()
#df['1360'] = data_1360[0].resample('MS',how=np.mean)['1360']#.fillna(method = 'ffill')
df['390'] = data_390[0]['390']
df['369'] = data_369[0]['369']
df['3310'] = data_3310[0]['3310']
df = df.fillna(method = 'ffill')

para = 6
Index_df = (df - df.mean())/ (df.max() - df.min())
Index_df = Index_df.dropna()
#Index_df['1360'] = Index_df['1360'] * 0.1
Index_df['390'] = Index_df['390'] * 0.2
Index_df['369'] = Index_df['369'] * 0.4
Index_df['3310'] = Index_df['3310'] * 0.4

MM_index = Index_df.sum(axis = 1)*100.
MM_index.name = 'MM'

Date_shift = pd.concat([MM_index,TWSE],axis=1)

Date_shift = Date_shift['MM'].shift(1).dropna()

Save.Save_SeriesData('mm-taiwan-stock-index',Date_shift)
#print pd.concat([data_390,data_369,data_3310,data_1360],axis=1)
'''