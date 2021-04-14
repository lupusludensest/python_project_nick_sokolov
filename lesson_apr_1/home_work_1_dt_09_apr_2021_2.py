# -*- coding: utf-8 -*-
import requests
import time
import winsound
freq, duration  = 440, 2000   # Hz/milliseconds

def price_tracking():
    starting_price = 0
    while True:
        bitcoin_api_url = 'https://api.bittrex.com/v3/markets/BTC-USD/ticker'
        response = requests.get(bitcoin_api_url)
        response_json = response.json()
        if response.ok: # A boolean indicating whether the response was successful (status in the range 200–299) or not
            current_price = float(response_json['lastTradeRate']) # 'lastTradeRate' is a key used as an index
            if starting_price == 0:
                starting_price = current_price
                print(f'Current price: "{current_price}"')
            elif starting_price >= current_price:
                print(f'Current price does not grow or failed for "{round((starting_price - current_price), 2)}"')
            elif starting_price < current_price:
                winsound.Beep(freq, duration)
                print(f'Current price "{current_price}" is more than previous price, it rised by "{round((current_price - starting_price), 2)}"')
            starting_price = current_price
        else:
            print(f'Server responce code "{response.status_code}"') # returns a number that indicates the status (200 is OK, 404 is Not Found).
        time.sleep(20)

print(price_tracking())