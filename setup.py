import pprint
import pandas as pd
import configparser
import oandapy


config = configparser.ConfigParser()
config.read('./config/config.ini')

account_id = config['oanda']['account_id']
api_key = config['oanda']['api_key']

# Get prices
oanda = oandapy.API(environment="practice", access_token=api_key)

response = oanda.get_prices(instruments="EUR_USD,USD_JPY,GBP_USD")

data = response['prices']
time_stamp = data[0]['time']
instrument = data[0]['instrument']
bid_price = data[0]['bid']
ask_price = data[0]['ask']

print("[{}] {} bid={} ask={}".format(time_stamp, instrument, bid_price, ask_price))


table = pd.DataFrame(response['prices'])
pprint.pprint(table)


response = oanda.get_instruments(account_id)
pd.DataFrame(response['instruments']).head()


