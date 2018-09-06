import nsepy as ns
import datetime as d
import pandas as pd
#s=ns.get_history(symbol='NIFTY IT', start=d.date(2015,1,1), end=d.date(2015,1,10), index = True)
s=ns.get_history(symbol='INFY', start=d.date(2015,1,1), end=d.date(2016,1,1))
file_name='dataset.csv'
s[['Open','Close','Low','High','Volume']].to_csv(file_name, sep=',', encoding='utf-8')
s1=ns.get_history(symbol='TCS', start=d.date(2015,1,1), end=d.date(2016,1,1))
with open('dataset.csv', 'a', encoding='utf-8') as f:
    s1[['Open','Close','Low','High','Volume']].to_csv(f, header=False)
s2=ns.get_history(symbol='NIFTY IT', start=d.date(2015,1,1), end=d.date(2016,1,1), index = True)
with open('dataset.csv', 'a', encoding='utf-8') as f:
    s2[['Open','Close','Low','High','Volume']].to_csv(f, header=False)

s[['Open','Close','Low','High','Volume']].to_csv('infy.csv', sep=',', encoding='utf-8')
s1[[ 'Open','Close','Low','High','Volume']].to_csv('tcs.csv', sep=',', encoding='utf-8')
s2[['Open','Close','Low','High','Volume']].to_csv('niftyit.csv', sep=',', encoding='utf-8')
