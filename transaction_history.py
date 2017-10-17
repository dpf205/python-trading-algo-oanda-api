import pandas as pd
import oandapyV20
import oandapyV20.endpoints.transactions as trans
import configparser

config = configparser.ConfigParser()
config.read('./config/config_v20.ini')
accountID = config['oanda']['account_id']
access_token = config['oanda']['api_key']

client = oandapyV20.API(access_token=access_token)


"""
# 1 Get transaction list
"""
r = trans.TransactionList(accountID)
client.request(r)

params = {
    "type": "MARKET_ORDER"
}
r = trans.TransactionList(accountID, params=params)
client.request(r)

"""
# 2 Get the details of a single transaction (they can be extracted individually as a pandas dataframe and stored in a database)
"""
r = trans.TransactionDetails(accountID=accountID, transactionID=49)
client.request(r)

# iterate through output of transactions
for oo in range(10, 20):
    r = trans.TransactionDetails(accountID=accountID, transactionID=oo)
    print(client.request(r))

