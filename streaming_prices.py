import json
from oandapyV20 import API
from oandapyV20.exceptions import V20Error
from oandapyV20.endpoints.pricing import PricingStream
import configparser


config = configparser.ConfigParser()
config.read('../config/config.ini')
accountID = config['oanda']['account_id']
access_token = config['oanda']['api_key']

api = API(access_token=access_token, environment="practice")

instruments = "EUR_USD, USD_JPY"
s = PricingStream(accountID=accountID, params={"instruments": instruments})

# format output to  JSON
try:
    n = 0
    for R in api.request(s):
        print(json.dumps(R, indent=2))
        n += 1
        if n > 5:
            print("done")
            break

except V20Error as e:
    print("Error: {}".format(e))