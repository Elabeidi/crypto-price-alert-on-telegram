import requests 
import time 

#global var

api_key="" # add api key from coinmarket cap
bot_key="" #bot api from telegram
chat_id= "" # chat id from telegram
limit = 50000
time_interval = 5

def get_price():
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    parameters = {
    'start': '1',
    'limit': '100',
    'convert': 'USD'}
    headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': '8df5931e-9eea-497d-a42e-dc181e42f378',}

    response = requests.get(url, headers=headers,params=parameters).json()
    btc_price = response['data'][0]['quote']['USD']['price']
    return btc_price
    
   
def send_update(chat_id, msg):
    url = f"https://api.telegram.org/bot{bot_key}/sendMessage?chat_id={chat_id}&text={msg}"
    requests.get(url)
    
def main():
    while True:
        price = get_price()
        print (price)
        if price > limit:
            send_update(chat_id, f"btc price going down:{price}")
        time.sleep(time_interval)
        
main()