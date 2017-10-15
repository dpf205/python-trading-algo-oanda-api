import pandas as py
import oandapyV20
import oandapyV20.endpoints.trades as trades
import configparser

config = configparser.ConfigParser()
config.read('../config/config_v20.ini')
accountID = config['oanda']['account_id']
access_token = config['oanda']['api_key']

"""
# 1 Get list of current trades for an account
"""
client = oandapyV20.API(access_token=access_token)

params = {
    "instrument": "DE30_EUR,EUR_USD"
}

# params are optional. use to retrieve trades for specific currency pair(s)
r = trades.TradesList(accountID=accountID, params=params)
client.request(r)
print(r.response)


"""
# 2 Get the list of open Trades for an Account.¶
"""
r = trades.OpenTrades(accountID)
client.request(r)
trade_id = r.response['trades'][0]['id']
print(trade_id)


"""
# 3 Get the details of a specific Trade in an Account.
"""
r = trades.TradeDetails(accountID, tradeID=trade_id)
client.request(r)
print(r.response)


"""
# 4 Close (partially or fully) a specific open Trade in an Account.
"""
#  close JUST PART  of position
data = {
    "units": 100 # this specifies the size of position to close, assuming the size is greater than 100 units
}
r = trades.TradeClose(accountID, tradeID=trade_id, data=data)
client.request(r)

# close ENTIRE position
r = trades.TradeClose(accountID, tradeID=trade_id)
client.request(r)