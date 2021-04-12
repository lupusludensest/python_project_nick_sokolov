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
        if response.ok:
            current_price = float(response_json['lastTradeRate'])
            if starting_price == 0:
                starting_price = current_price
                print(f'Current price: "{current_price}"')
            elif starting_price >= current_price:
                print(f'Current price does not grow or failed.')
            elif starting_price < current_price:
                winsound.Beep(freq, duration)
                print(f'Current price "{current_price}" > previous price, price rised for "{round((current_price - starting_price), 2)}"')
            starting_price = current_price
        else:
            print(f'Server responce code "{response.status_code}"')
        time.sleep(20)

print(price_tracking())
print(price_tracking())


