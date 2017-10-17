import pandas as pd
import oandapyV20
import oandapyV20.endpoints.instruments as instruments
import configparser

config = configparser.ConfigParser()
config.read('./config/config_v20.ini')
accountID = config['oanda']['account_id']
access_token = config['oanda']['api_key']

client = oandapyV20.API(access_token=access_token)

"""
 extract candlestick data:
 http://developer.oanda.com/rest-live-v20/instrument-df/#CandlestickGranularity
"""


params = {
          "count": 250,
          "granularity": "D"
}
r = instruments.InstrumentsCandles(instrument="EUR_USD", params=params)

client.request(r) # ouputs a large JSON object

r.response['candles'][0]['mid'] # outputs an object with open, high, low, close information when on print()
r.response['candles'][0]['time'] # outputs a time stamp  on print()
r.response['candles'][0]['volume'] # outputs the current volume value on print()

dat = []
for oo in r.response['candles']:
    dat.append([oo['time'], oo['volume'], oo['mid']['o'], oo['mid']['h'], oo['mid']['l'], oo['mid']['c']])

# output time,  open, high, low, close in a table
df = pd.DataFrame(dat)
df.columns = ['Time', 'Volume', 'Open', 'High', 'Low', 'Close']
df = df.set_index('Time')
df.head()