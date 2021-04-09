# Домашнее задание к уроку №1.
# Немного переработал ее, но суть осталась прежней.
# 1. [Обязательно] Нужно сделать бесконечный цикл в котором будет запрашиваться тикер='BTC-USD'
# с криптобиржи Bittrex через Rest API, используем следующий эндпоинт:
# https://api.bittrex.com/v3/markets/BTC-USD/ticker
# В конце цикла обязательно ставим задержку по времени time.sleep(30), можно и 15 сек поставить,
# но лучше не частить, т.к. биржа может забанить. В случае роста цены (lastTradeRate)
# от последней проверки, выдаем сообщение об этом.
# 2. [Дополнительно] Сделать возможность принимать тикер через аргумент командной строки,
# т.е. чтобы тикер задавался при вызове скрипта, например: python myscript.py 'LTC-USD'
# 3. [Дополнительно] При наступлении события роста, помимо сообщения издавать звуковой
# сигнал (прикреплю его, но можете найти свой). Для реализации я советую
# использовать библиотеку playsound, но можете найти альтернативу.
# Возможно на MacOS потребуется поставить дополнительно библиотеку pyobjc, она обеспечивает мост между python и objective-c, требуется для работы некоторых библиотек, в частности для playsound. Все библиотеки ставим как на уроке, через пакетный менеджер pip.
# Помните, знать это хорошо, но уметь быстро находить информацию еще лучше!

import requests
import time
import winsound
duration = 1000  # milliseconds
freq = 340  # Hz


url = "https://api.bittrex.com/v3/markets/BTC-USD/ticker"
data = requests.get(url)
data_json = dict(data.json())

print(f'Total there are: "{len(data_json)}" strings in json, type of data_json is {type(data_json)}')

print(f'{"*"*80}') # Just delimeter

res = dict((k, data_json[k]) for k in ['symbol', 'lastTradeRate'] if k in data_json)
print(res)

# for k in ['symbol', 'lastTradeRate']:
#     if k(time n + 1) > k(time n):
#         return (k(time n + 1), winsound.Beep(freq, duration))
#         time.sleep(20)



print(f'{"*"*80}') # Just delimeter