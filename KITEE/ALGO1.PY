import yfinance as yf
import pandas as pd
import talib as ta
from datetime import datetime
import time
import kiteSettings
from kiteconnect import KiteConnect
import logging





#---testing--------------------



#data=yf.download(tickers="RELIANCE.NS",period="59d",interval="5m")






def symbols_backtesting(symbol_list):
  for symbol in symbol_list:

        #df = yf.Ticker(f"{symbol}.NS").history(period="7d", interval="1m")
        df = yf.Ticker(symbol).history(period="3d", interval="1m")
        df.reset_index(inplace=True)
        df['Stocks']=symbol
        #df.drop(['Open','High','Low','Volume','Dividends','Stock Splits'],axis=1,inplace=True)
        Close=df['Close']                                                                #FETCHING CLOSE COLOMN
        rsi=ta.RSI(Close,14)                                                             #ADDING RSI INDICATOR & CREATING LIST OF RSI VALUES
        df['Rsi']=rsi 
        Volume=df['Volume']
        volume=ta.MA(Volume,5)
        df['Volume_Avg']=volume
        vol_div=round(df['Volume'][len(df)-2]/df['Volume_Avg'][len(df)-2],1)
        trade_open=0
        ENTRY=0
        
#-----------------------------------------1-MINUTE----------------------------------------#

        if df['Rsi'][len(df)-1] > 70 and vol_div>5 :
            print(df['Stocks'][len(df)-1],"||",df['Datetime'][len(df)-1],"||",int(df['Rsi'][len(df)-1]),"||",df['Close'][len(df)-1],"||","||",vol_div)




#------------------------------------------------------------------------------------------#

            """ENTRY=df['Close'][len(df)-1]
            LOSS_BOOK=df['Low'][len(df)-2]
            QUANTITY=int(20000/ENTRY)
            PROFIT_RATE=ENTRY+ENTRY/100
            DF1=df['High'][len(df)-1]-df['Low'][len(df)-1]
            DF2=df['High'][len(df)-2]-df['Low'][len(df)-2]
            DF3=df['High'][len(df)-3]-df['Low'][len(df)-3]"""
            
            def order_place():
                kite = KiteConnect(kiteSettings.api_key)
                kite.set_access_token(kiteSettings.access_token)
                try:
                    
                    order_id = kite.place_order(tradingsymbol=df['Stocks'][len(df)-1][0:-3],
                                            exchange=kite.EXCHANGE_NSE,
                                            transaction_type=kite.TRANSACTION_TYPE_BUY,
                                            quantity=1,
                                            #price=df['Close'][len(df)-1],
                                            variety=kite.VARIETY_REGULAR,
                                            order_type=kite.ORDER_TYPE_MARKET,
                                            product=kite.PRODUCT_MIS)
                    
                    logging.info("Order placed. ID is: {}".format(order_id))
                except Exception as e:
                    logging.info("Order placement failed: {}".format(e.message))
                return order_id                    
            order_place()
            def loss_place():
                    kite = KiteConnect(kiteSettings.api_key)
                    kite.set_access_token(kiteSettings.access_token)
                    try:
                    
                        order_id = kite.place_order(tradingsymbol=df['Stocks'][len(df)-1][0:-3],
                                                exchange=kite.EXCHANGE_NSE,
                                                transaction_type=kite.TRANSACTION_TYPE_SELL,
                                                quantity=1,
                                                price=LOSS_BOOK,
                                                trigger_price=LOSS_BOOK,
                                                variety=kite.VARIETY_REGULAR,
                                                order_type=kite.ORDER_TYPE_SL,
                                                product=kite.PRODUCT_MIS)
                        
                        logging.info("Order placed. ID is: {}".format(order_id))
                    except Exception as e:
                        logging.info("Order placement failed: {}".format(e.message))
                    return order_id
            loss_place()
            trade_open=0
                    

 

                                                             

from stocks_list import symbol_list as symbol_list
for i in range(0,100000):
    symbols_backtesting(symbol_list)
    print("------------------------------------------------------------------------------------------------------")
    time.sleep(30)



            
                
 

            
        
       
       




