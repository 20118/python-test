import csv
import numpy as np
def main():
    k=0
    i=0
    j=0
    try:
            ## first week conversion is done(5 days = 1 week)
            size = sum(1 for l in open('infy.csv'))
            length=size
            date,openp,close,low,high,volume =np.loadtxt('infy.csv',unpack=True,delimiter=',',dtype='str',skiprows=0)
            while(i<length):
                    savefile=open('week_conversion.csv','a+')
                    savepoint=date[i]+','+str(openp[i])+','+str(close[i])+','+str(low[i])+','+str(high[i])+','+str(volume[i])+'\n'
                    savefile.write(savepoint)
                    i=i+1

            week4=4
            week16=16
            week52=52
            size = sum(1 for l in open('week_conversion.csv'))
            length=size
            print(size)
            while(k<length):
                sma4=sma(k,week4)                                #there should be loop from 4 to 52 (difference of 4)
                #sma16=SMA_week(k,week16)
                #sma52=SMA_week(k,week52)
                k=k+1
                savepoint1=date[k-1]+','+str(sma4)+'\n'
                savefile=open('sma4.csv','a+')
                #savepoint2=date[k-1]+','+str(sma16)+'\n'
                #savefile=open('sma4.csv','a+')
                #savepoint3=date[k-1]+','+str(sma52)+'\n'
                #savefile=open('sma52.csv','a+')
                print (savepoint1)
                savefile.write(savepoint1)
                savefile.close

    except IOError:
        print("Error")

def sma(j,week):  #calculate the simple moving average for each data entry
    date,openp,close,low,high,volume =np.loadtxt('week_converstion.csv',unpack=True,delimiter=',',dtype='str',skiprows=0)
    sum1=0.00
    size = sum(1 for l in open('week_conversion.csv'))
    length=size
    while(j<(j+week)):
        if(j<=length):
            sum1=sum1+float(openp[i])
    sma=sum1/week
    return sma

main()
