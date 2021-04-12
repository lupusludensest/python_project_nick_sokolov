import requests
import time
import winsound
freq = 440  # Hz
duration = 2000  # milliseconds

bitcoin_api_url = 'https://api.bittrex.com/v3/markets/BTC-USD/ticker'

def btn_rate():
    response = requests.get(bitcoin_api_url)
    response_json = response.json()
    return float(response_json['lastTradeRate'])

def price_tracking():
    starting_price = 0
    while True:
        response = requests.get(bitcoin_api_url)
        if response.ok:
            current_price = btn_rate()
            if starting_price == 0:
                starting_price = current_price
                print(f'Current price: "{current_price}"')
            elif starting_price >= current_price:
                print(f'Current price does not grow.')
            elif starting_price < current_price:
                winsound.Beep(freq, duration)
                print(f'Current price "{current_price}" > Starting price, price rised for "{round((current_price - starting_price), 2)}"')
        else:
            print(f'Server responce code "{response.status_code}"')
        time.sleep(20)

print(price_tracking())


