import pandas as pd
def MA(nday,a):
    print("in function")
    SMA = pd.Series((a['Close']).rolling(window=ndays).mean(),name = 'SMA')
    
    a = a.join(SMA)
    a = a.fillna(0) 
    return a

stock=input("Choose the dataset: tcs or infy \n")
stockdata=pd.read_csv(stock+'.csv')
week=[4,8,16,32,52]

#week=int(input("Enter the weeks in range 4,8,16,32,52\n"))
for i in range(0,(len(week)-1)):
    
    ndays=week[i]*5
    print("before function")
    a=MA(ndays,stockdata)

a.to_csv(stock+'_new.csv')

'''
caclute the volume shock and including a column name volume shocks in the data
'''
shock=[]
shock.append(0)
for i in range(1,len(a['Volume'])):
    flag=0
    x1=a.iloc[i,10]
    x2=a.iloc[i-1,10]
    if x1>x2:
        diff=1.1*x2
        if x1>diff:
            flag=1
        
    else:
        diff=0.9*x2
        if x1<diff:
            flag=1
    shock.append(flag)
    
a['Volume Shocks']=shock
print("volume shock calulated")
'''
caclute the price shock and including a column name price shocks in the data
'''
shock=[]
for i in range(0,len(a['Close'])):
    flag=0
    x1=a.iloc[i,8]
    x2=a.iloc[i,3]
    if x1>x2:
        diff=1.02*x2
        if x1>diff:
            flag=1
        
    else:
        diff=0.98*x2
        if x1<diff:
            flag=1
    shock.append(flag)
    
a['Price Shocks']=shock
print("price shock calulated")

'''
caclute the Pricing shock without volume shock and including a column name Pricing shock without volume shock in the data
Pricing shock without volume shock
'''
shock=[]
for i in range(0,len(a['Close'])):
    if a.iloc[i,16]==0 and a.iloc[i,17]==1:
        shock.append(1)
    else:
        shock.append(0)
a['Pricing shock without volume shock']=shock

 # Creating a 0/1 dummy-coded time series for direction of shocks.       
a = pd.get_dummies(a, columns=['Volume Shocks','Price Shocks','Pricing shock without volume shock'])
a.to_csv(stock+'final_partOne.csv')



    


