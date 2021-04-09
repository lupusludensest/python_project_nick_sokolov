import requests
import time


url = "https://api.bittrex.com/v3/currencies"
data = requests.get(url)
data_json = data.json()

print(f'Total there are: "{len(data_json)}" strings in json, type of data_json is {type(data_json)}')

print(data_json[0], '\n')
# print(data_json[1]['symbol'], '\n')
# print(data_json[1]['name'], '\n')

for symbol in data_json:
    print(symbol['name'])
    time.sleep(0.0000000001)

# while True:
#     print(f'Hello,')
#     time.sleep(3)
#     print(f'world!')

# Home work 1, endless while loop, with sound, BTC/USD
# https://bittrex.github.io/api/v3
# http://jsonviewer.stack.hu/
# https://api.bittrex.com/v3/currencies
# https://api.bittrex.com/v3/currencies/4ART
# https://api.bittrex.com/v3/markets/BTC-USD/ticker