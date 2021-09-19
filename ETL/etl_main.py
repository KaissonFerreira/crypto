#%%
from dotenv.main import find_dotenv
import pandas as pd
import pandas_gbq
import numpy as np

from google.oauth2 import  service_account
from google.cloud import bigquery
from binance import Client

import os
from dotenv import load_dotenv
#%%

# Carregando as chaves para conectar as API's do GCP e da Binance
load_dotenv('ETL\.env')
#%%
# GCP
project_id = os.getenv('project_id')
credentials = service_account.Credentials.from_service_account_file('GCP.json')
#%%
# Binance
api_key =os.getenv('api_key')
api_security = os.getenv('api_security')

client = Client(api_key=api_key,api_secret=api_security)
#%%
# Extração de dados das criptomoedas
# BTC
btc = np.array(client.get_historical_klines(symbol="BTCBRL", interval=Client.KLINE_INTERVAL_1HOUR, start_str="1 jan, 2019"))
#%%
df_btc = pd.DataFrame(btc,dtype=float, columns= ('Open_time', 
                                                    'Open', 
                                                    'High', 
                                                    'Low', 
                                                    'Close', 
                                                    'Volume',
                                                    'Close_Time',
                                                    'Quot_asset_volume',
                                                    'Number_of_traders',
                                                    'Taker_buy_base_asset',
                                                    'Taker_buy_quote_asset',
                                                    'Ignore'))



# %%
df_btc['Open_time'] = pd.to_datetime(df_btc['Open_time'], unit='ms').dt.tz_localize('UTC').dt.tz_convert('America/Sao_Paulo')
# %%
df_btc
# %%
