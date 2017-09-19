import pprint
import pandas as pd
import oandapyV20
import oandapyV20.endpoints.accounts as accounts
import configparser

# get account details
config = configparser.ConfigParser()
config.read('./config/config.ini')
accountID = config['oanda']['account_id']
access_token = config['oanda']['api_key']

client = oandapyV20.API(access_token=access_token)

#  Get Basic Account Details
r = accounts.AccountDetails(accountID)

client.request(r)
account_details = r.response
print("\n raw account details: \n", account_details)
# or
account_table_format = pd.Series(r.response['account'])
print(account_table_format)

# Get Account List (for tracking multiple aub accounts)
r = accounts.AccountList()
all_acc_under_mgt = client.request(r)
print("\n All Accounts under management: \n", all_acc_under_mgt)

# Get Account Status Summary (are there open trades?... etc)
r = accounts.AccountSummary(accountID)
client.request(r)
account_status_summary = pd.Series(r.response['account'])
print("\n Summary  of Account Status: \n", account_status_summary)

# Instruments that can be traded with the specified account,
# minimum Trailing Stop Distance,
r = accounts.AccountInstruments(accountID=accountID, params="EUR_USD")
client.request(r)
account_instruments = pd.DataFrame(r.response['instruments'])
print("\n List of tradable Account Instruments: \n", account_instruments)