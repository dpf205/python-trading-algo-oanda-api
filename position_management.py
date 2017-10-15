import pandas as pd
import oandapyV20
import oandapyV20.endpoints.positions as positions
import configparser

config = configparser.ConfigParser()
config.read('../config/config_v20.ini')
accountID = config['oanda']['account_id']
access_token = config['oanda']['api_key']

client = oandapyV20.API(access_token=access_token)


"""
# 1 List all Positions included pending limit orders AND currently active market orders to the account and their P/L status
"""
r = positions.PositionList(accountID=accountID)
client.request(r)
# print(client.request(r))

"""
# 2 List all current OPEN market order positions with current trades and their P/L status.
"""
r = positions.OpenPositions(accountID=accountID)
client.request(r)

"""
# 3 Get the details of a SINGLE instrument’s current open position in an Account (excellent for automating/assessing risk-management strategies)
"""
instrument = "AUD_USD"
r = positions.PositionDetails(accountID=accountID, instrument=instrument)
client.request(r)

"""
# 4 Closeout ALL  open positions for an instrument in an Account.
"""
data = {
  "longUnits": "ALL",
  "shortUnits": "ALL"
}
r = positions.PositionClose(accountID=accountID, instrument=instrument, data=data)
client.request(r)
