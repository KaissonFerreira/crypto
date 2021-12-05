from os import environ as en

#GCP
CREDENTIALS_GCP = en["GCP"]
PROJECT_ID = 'black-resource-334223'
DATASET = 'Dataset_cripto'

# My SQL e SQLAchemy
KEY_SQL = en['SENHA']
HOST = '127.0.0.1'
USER = 'root'
DATABASE = 'crypto-project'

#API Binance
KEY = en["KEY_BINANCE"]
SECRET=en["SECRET_BINANCE"]

# Lista das crypto
LIST_CRIPTO = {'ETH':'Ethereum',
                'BTC':'Bitcoin',
                'ADA':'Cardano',
                'DOT':'Polkadot',
                'SOL':'Solano',
                'BTT':'BitTorrent',
                'MANA':'Decentraland',
                'AXS':'Axie Infinity',
                'LUNA':'Terra',
                'MATIC':'Polygon',
                'AVAX':'Avalanche'}

