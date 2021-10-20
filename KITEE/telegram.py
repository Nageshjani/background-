import requests

def tele(bot_message):
    #bot_token='2091875523:AAGRcEOUlblBZVyW7DLXZFny4hXdkN2er9Q',
    # bot_id='	1427812863',
    url = "https://api.telegram.org/bot2091875523:AAGRcEOUlblBZVyW7DLXZFny4hXdkN2er9Q/sendMessage?chat_id=1427812863&text="+bot_message
    return requests.post(url)



tele("jj")





