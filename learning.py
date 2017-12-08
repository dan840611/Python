#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  4 20:55:11 2017

@author: Dan
"""

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

'''
y = np.random.standard_normal(20)
y2 = y * 100


plt.plot(y.cumsum(), 'b', lw = 1.5, label='1st')
plt.plot(y.cumsum(), 'ro')

plt.plot(y, 'r', label = '2nd')

#參數： tight 所影數據可見；[xmin, xmax, ymin, ymax]
plt.axis('tight')
plt.xlabel('index')
plt.ylabel('value')
plt.title('Practice')

# 0 為最佳位置
plt.legend(loc=0)


#雙座標軸
ax1 = plt.subplots()
plt.plot(y.cumsum(), 'b', label = '1st')
plt.plot(y.cumsum(), 'ro')
plt.xlabel('x')
plt.ylabel('y')
plt.axis('tight')
plt.legend(loc=0)
plt.grid(True)

ax2 = ax1.twinx()
plt.plot(y2, 'r', label = '2st')
plt.legend(loc = 0)
plt.ylabel('2nd y ')

#多圖

plt.subplot(211) #121
plt.plot(y.cumsum(), 'b', label = '1st')
plt.plot(y.cumsum(), 'ro')
plt.xlabel('x')
plt.ylabel('y')
plt.axis('tight')
plt.legend(loc=0)
plt.grid(True)

plt.subplot(212) #122
plt.plot(y2, 'r', label = '2st')
plt.legend(loc = 0)
plt.ylabel('2nd y ')
'''

'''

##############################
#scatter
y = np.random.standard_normal((1000, 2))


c = np.random.randint(0 , 10, len(y))

plt.scatter(y[:, 0], y[:, 1]  , c = c, marker = 'o')
plt.colorbar()
plt.xlabel('x')
plt.ylabel('y')
plt.axis('tight')
plt.title('test')
plt.legend(loc=0)
plt.grid(True)



#histogram

plt.hist(y, label= ['1st', '2nd'], bins = 25)
plt.xlabel('x')
plt.ylabel('y')
plt.axis('tight')
plt.title('test')
plt.legend(loc=0)
plt.grid(True)

#boxplot

plt.boxplot(y)
plt.grid(True)
plt.setp(ax, xticklabels = ['1st', '2nd'])
plt.xlabel('dataset')
plt.ylabel('valur')
plt.title('Boxplot')

'''

#finance plot

import matplotlib.finance as mpf

start = (2010, 1, 1)
end = (2017, 9, 22)
quotes = mpf.quotes_historical_yahoo_ochl('^GDAXI', start, end)