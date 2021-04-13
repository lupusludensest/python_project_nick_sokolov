import requests
import time
import winsound
freq = 440  # Hz
duration = 2000  # milliseconds
import sys

class CryptoTracker:

    def __init__(self, currencies="BTC-USD"):
        self.currencies_pair = currencies
        self.END_POINT = f"https://api.bittrex.com/v3/markets/{self.currencies_pair}/ticker"
        self.initial_price = 0

    def track_changes(self):
        print(f"The script let you know if the price for {self.currencies_pair} will go up.")
        while True:
            response = requests.get(self.END_POINT)
            if response.ok:
                new_price = float(response.json()['lastTradeRate'])
                if self.initial_price == 0:
                    self.initial_price = new_price
                    print(f"Starting price is {new_price}")
                elif self.initial_price >= new_price:
                    print("Please be patient, the price is the same or getting lower (update every 30 sec.)")
                elif self.initial_price < new_price:
                    print(
                        f"The price for {self.currencies_pair} went up by {round(new_price - self.initial_price, 2)}. "
                        f"The new price is: {new_price}")
                    winsound.Beep(freq, duration)
                self.initial_price = new_price
            else:
                print(f"Something went wrong. Response code = {response.status_code}")
            time.sleep(20)

if len(sys.argv) > 1: #  is the number of command-line arguments.
    CryptoTracker(sys.argv[1]).track_changes() #  is the program script name
    print(CryptoTracker(sys.argv[1]).track_changes())
else:
    CryptoTracker().track_changes()
    print(CryptoTracker().track_changes())