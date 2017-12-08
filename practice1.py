#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 12 20:03:11 2017

@author: Dan
"""
import pandas as pd


##
year = [1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022]
value = []
date =  []

# Create year-row-index:
url = "http://www.imf.org/external/pubs/ft/weo/2017/01/weodata/weorept.aspx?sy=1996&ey=2022&scsm=1&ssd=1&sort=country&ds=.&br=1&pr1.x=70&pr1.y=6&c=924%2C576%2C132%2C134%2C528%2C158%2C112%2C542%2C111&s=NGDPD&grp=0&a="

df = pd.read_html(url)[4]
df = df.ix[2:10, :]
    
    
for i in range(1996, 2023, 1):
    time = str(i) + '-' + '01' + '-' + '01' 
    date.append(time)


# Create df:
for k in range(2, 11, 1):
    value.append(df.ix[k, 5:])
    value[k-2].index = date
    if k==2 :
        df0= pd.DataFrame({df.ix[k,0]: value[0]}, index=date)
    else :
        df1= pd.DataFrame({df.ix[k,0]: value[k-2]}, index=date)
    df0 = pd.concat([df0, df1], axis=1)   
