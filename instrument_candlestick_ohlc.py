import pandas as pd
import oandapyV20
import oandapyV20.endpoints.instruments as instruments
import configparser

config = configparser.ConfigParser()
config.read('config/config.ini')
accountID = config['oanda']['account_id']
access_token = config['oanda']['api_key']

client = oandapyV20.API(access_token=access_token)

params = {
          "count": 5,
          "granularity": "M5"
}

r = instruments.InstrumentsCandles(instrument="DE30_EUR", params=params)

client.request(r)
print(r.response) # displays flat JSON object of OHLC, time, and volume

candlestick_attrib = r.response['candles']
print(candlestick_attrib) # displays JSON object of OHLC, time, and volume data