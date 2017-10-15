import pandas as pd
import configparser
import oandapyV20
from oandapyV20 import API
import oandapyV20.endpoints.pricing as pricing

config = configparser.ConfigParser()
config.read('./config/config.ini')
accountID = config['oanda']['account_id']
access_token = config['oanda']['api_key']
api = API(access_token=access_token)

# Get rates information
params = {"instruments": "EUR_USD,USD_JPY"}

r = pricing.PricingInfo(accountID=accountID, params=params)

rv = api.request(r)

print(r.response)

prices = pd.DataFrame(r.response['prices'])

print(prices)

