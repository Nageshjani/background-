
import kiteSettings
from kiteconnect import KiteConnect
import logging
stocks=['RELIANCE','INFY','ITC']
def order_place():
    kite = KiteConnect(kiteSettings.api_key)
    kite.set_access_token(kiteSettings.access_token)
    try:
	    
        order_id = kite.place_order(tradingsymbol="AXISBANK",
                                exchange=kite.EXCHANGE_NSE,
                                transaction_type=kite.TRANSACTION_TYPE_SELL,
                                quantity=1,
                                #trigger_price=791.5,
                                #price=791.5,
                                variety=kite.VARIETY_REGULAR,
                                order_type=kite.ORDER_TYPE_MARKET,
                                product=kite.PRODUCT_MIS)
        
        logging.info("Order placed. ID is: {}".format(order_id))
    except Exception as e:
    	logging.info("Order placement failed: {}".format(e.message))
    
    return order_id

#---testing--------------------

result = order_place()

print("------------------")
print(result)



var=5
if var==5:
    order_place()