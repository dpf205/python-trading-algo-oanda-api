import oandapyV20
import oandapyV20.endpoints.instruments as instruments
import configparser

config = configparser.ConfigParser()
config.read('./config/config_v20.ini')
accountID = config['oanda']['account_id']
access_token = config['oanda']['api_key']

client = oandapyV20.API(access_token=access_token)
"""
# r = instruments.InstrumentsOrderBook(instrument="EUR_USD", params=params) 
params are an optional request query parameters, check developer.oanda.com for details
"""
params = {
    # optional values
}

r = instruments.InstrumentsOrderBook(instrument="EUR_USD")
client.request(r)