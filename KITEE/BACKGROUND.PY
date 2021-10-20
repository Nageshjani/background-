import yfinance as yf
import pandas as pd
import talib as ta
from datetime import datetime
import time
import kiteSettings
from kiteconnect import KiteConnect
import logging
import requests

def tele(bot_message):
    #bot_token='2091875523:AAGRcEOUlblBZVyW7DLXZFny4hXdkN2er9Q',
    # bot_id='	1427812863',
    url = "https://api.telegram.org/bot2091875523:AAGRcEOUlblBZVyW7DLXZFny4hXdkN2er9Q/sendMessage?chat_id=1427812863&text="+bot_message
    return requests.post(url)







#data=yf.download(tickers="RELIANCE.NS",period="59d",interval="5m")

activated_Stocks=[]
def symbols_backtesting(symbol_list):
  for symbol in symbol_list:
        #df = yf.Ticker(f"{symbol}.NS").history(period="7d", interval="1m")
        df = yf.Ticker(symbol).history(period="3d", interval="5m")
        df.reset_index(inplace=True)
        df['Stocks']=symbol
        #df.drop(['Open','High','Low','Volume','Dividends','Stock Splits'],axis=1,inplace=True)
        Close=df['Close']                                                                #FETCHING CLOSE COLOMN
        rsi=ta.RSI(Close,14)                                                             #ADDING RSI INDICATOR & CREATING LIST OF RSI VALUES
        df['Rsi']=rsi 
        Volume=df['Volume']
        volume=ta.MA(Volume,72)
        df['Volume_Avg']=volume
        vol_div=round(df['Volume'][len(df)-2]/df['Volume_Avg'][len(df)-2],1) 
        #print(df)
        #dabur
        #print("----------------------")

        #if df['Stocks'][len(df)-1] not in activated_Stocks:
        if  (df['Rsi'][len(df)-1]>70 or df['Rsi'][len(df)-1]<30)  and vol_div>0:
                MESSAGE=str(df['Datetime'][len(df)-1])+"||"+str(df['Stocks'][len(df)-1])+"||"+str(int(df['Rsi'][len(df)-1]))+"||"+str(vol_div)+"||"+str(round(df['Close'][len(df)-1],1))
                tele(MESSAGE)
                print(df['Datetime'][len(df)-1],df['Stocks'][len(df)-1],"||",int(df['Rsi'][len(df)-1]),"||",vol_div,"||",round(df['Close'][len(df)-1],1))

                

from stocks_list import symbol_list as symbol_list
for i in range(0,100000):
    symbols_backtesting(symbol_list)
    print("------------------------------------------------------------------------------------------------------")
    tele("------------------------------------------------------------------------------------------------------")
    time.sleep(5)






            
                
 

            
        
       
       





