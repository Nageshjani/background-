import kiteSettings
from kiteconnect import KiteConnect
import logging
from datetime import datetime
import pandas as pd
kite = KiteConnect(api_key=kiteSettings.api_key)


def quoteMethod(symbol):
    kite = KiteConnect(kiteSettings.api_key)
    kite.set_access_token(kiteSettings.access_token)
    #data=kite.historical(instrument_token='256265',from_date='2020-08-21',to_date='2021-08-21',interval='day')
    data=kite.historical_data(instrument_token='256265',from_date='2020-08-21',to_date='2021-08-21',interval="5 minutes")
    quote_details=pd.DataFrame(data)

    
    #quote_details=kite.quote(symbol,interva)
    #quote_details=kite.instruments(exchange='NSE')
    
    return quote_details



 
 

#symbol1='NFO:NIFTY21AUGFUT'
#symbol2='NFO:NIFTY21AUG15900CE'
symbol3='NSE:INFY'

details=quoteMethod(symbol3)

print(details)

#current_market_price=details['NFO:NIFTY21AUGFUT']['last_price']

#print("Current Market Price:", details)