import requests
import time


url = "https://api.bittrex.com/v3/currencies"
data = requests.get(url)
data_json = data.json()

print(f'There are: "{len(data_json)}" strings in json\n')

# print(data_json[0])
# print(data_json[1]['symbol'])
# print(data_json[1]['name'])

for i in data_json:
    print(i['name'])
    time.sleep(0)

# while True:
#     print(f'Hello,')
#     time.sleep(3)
#     print(f'world!')

# Home work 1, endless while loop, with sound, BTC/USD
# 1. https://bittrex.github.io/api/v3 open this choose json what you need, copy past it to url
# 2. https://api.bittrex.com/v3/currencies
# 3. https://api.bittrex.com/v3/currencies/4ART
# 4. https://api.bittrex.com/v3/markets/BTC-USD/ticker copy past ctr+a->ctrl+c->ctrl+v to
# 5. http://jsonviewer.stack.hu/ makes json readable, paste->format
