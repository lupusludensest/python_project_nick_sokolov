import requests
import time
import winsound
from datetime import datetime
duration = 1000  # milliseconds
freq = 440  # Hz

bitcoin_api_url = 'https://api.bittrex.com/v3/markets/BTC-USD/ticker'

# def get_latest_bitcoin_price():
#     response = requests.get(bitcoin_api_url)
#     response_json = response.json()
#     return f"{response_json['symbol']}: {float(response_json['lastTradeRate'])}"

def text_from():
    response = requests.get(bitcoin_api_url)
    response_json = response.json()
    return float(response_json['lastTradeRate'])

# Eternal loop
bitcoin_history = []
while True:
    date = datetime.now()
    bitcoin_history.append({'date': date, 'price': text_from()})
    print(bitcoin_history[-1].values())
    # if False:
    #     winsound.Beep(freq, duration)
    time.sleep(20)


