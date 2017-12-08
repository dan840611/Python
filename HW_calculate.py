
import pandas as pd

def read_mm(file):
    df = pd.read_csv(file,index_col=0, encoding = "ISO-8859-1")
    df.index = df.index.to_datetime()
    df['Value'] = df['Value'].astype('float')        
    return df

df1 = read_mm('mm_sin-exchange-rate.csv')
df2 = read_mm('mm_sin-composite-leading-index.csv')
df3 = read_mm('mm_singapore-non-oil-export-yoy.csv')
df4 = read_mm('mm_fx-usd-sgd.csv')
df5 = read_mm('mm_singapore-stock-index.csv')



df1 = df1['Value'].resample('MS',how='mean')
df4 = df4['Value'].resample('MS',how='mean')
df5 = df5['Value'].resample('MS',how='last')


df = pd.concat([df1,df2,df3,df4,df5], axis=1) 
df = df.fillna(method="ffill")
df = df.dropna()
df.columns = ['interest-rate', 'leading-index', 'export-growth-rate','fx', 'MSCI']



df['interest-rate'] = df['interest-rate']-df['interest-rate'].mean()/(df['interest-rate'].max()-df['interest-rate'].min())
df['leading-index'] = df['leading-index']-df['leading-index'].mean()/(df['leading-index'].max()-df['leading-index'].min())
df['fx'] = df['fx']-df['fx'].mean()/(df['fx'].max()-df['fx'].min())



df['MM-index'] = 0.1 * df['interest-rate'] -0.2 * df['fx'] + 0.5 * df['leading-index'] + 0.6 * df['export-growth-rate']-45


df0 = pd.DataFrame({'MM-index':df['MM-index'], 'MSCI':df['MSCI']}, index=df.index)

df01 = pd.DataFrame({'MM-index':df['MM-index']}, index=df.index)
df02= pd.DataFrame({ 'MSCI':df['MSCI']}, index=df.index)

df0.plot(second_y=True)


