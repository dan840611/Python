#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 22:14:27 2017

@author: Dan
"""

import numpy as np
import pandas as pd
import xlrd
import xlwt

#建立工作表
wb = xlwt.Workbook()

#加入一個工作表
wb.add_sheet('first_sheet', cell_overwrite_ok = True)

#取得工作表索引
wb.get_active_sheet()
ws_1 = wb.get_sheet(0)

#建立二個工作表
ws_2 = wb.add_sheet('second_sheet')

data = np.arange(1, 65).reshape((8,8))

#在A1寫100
ws_1.write(0, 0, 100)

#save    wb.save(path + 'workbook.xls')

export = xlrd.open_workbook('/Users/Dan/Desktop/twExport.xlsx')
export.sheet_names()

#取得sheet
export = export.sheet_by_name('twExport')
# export = export.sheet.shett_by_index(1)

#知道列、行資訊
export.ncols
export.nrows
export.cell(0,0)

#取得第二欄資訊
export.col(1)

#####################################################################
export = pd.read_excel('/Users/Dan/Desktop/twExport.xlsx', 'twExport', header = None)
export = pd.DataFrame({'Date' : export.iloc[1:,0], 'Value' : export.iloc[1:, 1]})

order = pd.read_excel('/Users/Dan/Desktop/twOrder.xlsx', header = None)
order = pd.DataFrame({'Date': order.iloc[1:, 0], 'Value': order.iloc[1:, 1]})

twii = pd.read_excel('/Users/Dan/Desktop/twii.xlsx', header = None)
twii = pd.DataFrame({'Date': twii.iloc[1:, 0], 'Value': twii.iloc[1:, 1]})


from bokeh.plotting import figure, output_file, show

output_file("patch.html")

p = figure(plot_width=400, plot_height=400)
p.multi_line(export, order,
             color=["firebrick", "navy"], alpha=[0.8, 0.3], line_width=4)


