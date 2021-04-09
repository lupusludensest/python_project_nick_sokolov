# Home work 1, endless while loop, with sound, BTC/USD
# 1. https://bittrex.github.io/api/v3 open this choose json what you need, copy past it to url
# 2. https://api.bittrex.com/v3/currencies
# 3. https://api.bittrex.com/v3/currencies/4ART
# 4. https://api.bittrex.com/v3/markets/BTC-USD/ticker copy past ctr+a->ctrl+c->ctrl+v to
# 5. http://jsonviewer.stack.hu/ makes json readable, paste->format

import requests
import time

url = "https://api.bittrex.com/v3/currencies"
data = requests.get(url)
data_json = data.json()

print(f'Total there are: "{len(data_json)}" strings in json')

print(f'{"*"*80}') # Just delimeter

for i in data_json:
    if "USD" in i["symbol"]:
        print(f'{i["symbol"]}: {i["minConfirmations"]}')
        time.sleep(0)

print(f'{"*"*80}') # Just delimeter

for i in data_json:
    if "BTC" in i["symbol"]:
        print(f'{i["symbol"]}: {i["minConfirmations"]}')
        time.sleep(0)

print(f'{"*"*80}') # Just delimeter

