import pandas as pd
import numpy as np
import config

from binance import Client


class Extract:
    """Classe para extrair dados da Binance"""
    def __init__(self, extract_binance):
        self.extract_binance = extract_binance
    def extract_binance(symbol=str,date='1 jan, 2019'):
        """O argumento utilizado para essa função é o símbolo da Crypto que vai ser convertido em reais. \n 
        Essa função busca apenas informações no intervalo de 1 hora desde 1 de janeiro de 2019."""

        print('\nIniciando a extração dos dados do criptoativo - {} ...'.format(symbol))
        client = Client(api_key=config.KEY,api_secret=config.SECRET)
        crypto = np.array(client.get_historical_klines(symbol=f'{symbol}BRL', interval=Client.KLINE_INTERVAL_1HOUR, start_str=f"{date}"))
        return crypto


#b = list(config.LIST_CRIPTO)[0]
#print(b)
#Extract.extract_binance(b)







