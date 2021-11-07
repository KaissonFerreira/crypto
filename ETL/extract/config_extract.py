
import pandas as pd
import pandas_gbq
import numpy as np

#BQ_google
from google.oauth2 import  service_account
from google.cloud import bigquery

#BD_Mysql
import mysql.connector


from binance import Client
import os
from dotenv import load_dotenv

# Carregando as chaves para conectar as API's do GCP e da Binance
load_dotenv('ETL\.env')


# Binance
api_key =os.getenv('api_key')
api_security = os.getenv('api_security')
client = Client(api_key=api_key,api_secret=api_security)
class Extract:
    """Classe para utilizar na extração dos dados da Binance"""
    def __init__(self, symbol) -> str:
        self.x = symbol
    def extract_binance(self):
        """O argumento utilizado para essa função é o símbolo da Crypto
        que vai ser convertido em reais. Essa função busca apenas informações no intervalo de 1 hora desde 1 de janeiro de 2019."""
        print('\nIniciando a extração dos dados do criptoativo {} ...'.format(self.x))
        crypto = np.array(client.get_historical_klines(symbol=f'{self.x}BRL', interval=Client.KLINE_INTERVAL_1HOUR, start_str="1 jan, 2019"))
        print('Realizando a transformação dos dados')
        df = pd.DataFrame(crypto,dtype=float, columns= ('Open_time', 
                                                            'Open', 
                                                            'High', 
                                                            'Low', 
                                                            'Close', 
                                                            'Volume',
                                                            'Close_time',
                                                            'Quot_asset_volume',
                                                            'Number_of_traders',
                                                            'Taker_buy_base_asset',
                                                            'Taker_buy_quote_asset',
                                                            'Ignore'))
        # Trasformand as colunas Open_time e Close_time em Datetime.
        df['Open_time'] = pd.to_datetime(df['Open_time'], unit='ms').dt.tz_localize('UTC').dt.tz_convert('America/Sao_Paulo')
        df['Close_time'] = pd.to_datetime(df['Close_time'], unit='ms').dt.tz_localize('UTC').dt.tz_convert('America/Sao_Paulo')

        # Realizando um slice só para algumas colunas
        df = df[['Open_time', 
                            'Open', 
                            'High', 
                            'Low', 
                            'Close', 
                            'Volume',
                            'Close_time',
                            'Number_of_traders']]

        # Criação de bandas de Bollinger
            # Média móvel das últimas 12 hrs
                # shift(1) é o valor anterior e o rolling de 12 horas
        df['Media_movel'] = df['Close'].shift(1).rolling(12).mean()
            # Desvio padrão das últimas 12 hrs 
        df['Desvio_P_12hours'] = df['Close'].shift(1).rolling(12).std()
            # Banda Inferior
        df['Banda_inf'] = df['Media_movel'] - 2*df['Desvio_P_12hours']
            # Banda Superior
        df['Banda_sup'] = df['Media_movel'] + 2*df['Desvio_P_12hours']

        return df

# GCP
# Função que envia os dados para o BQ.
def update_bq(df, table, dataset='crypto', if_exists = 'replace'):
    """ Essa função envia os dados processados para o BQ.
    df = DataFrame
    table = Nome da tabela
    dataset = Nome do Dataset
    if_exists = 'append' or 'replace' - default 'replace'"""
    print('Inciando o carregamento da tabela {}'.format(table))
    # Conectando com a API
    project_id = os.getenv('project_id')
    #path_json = 'C:\projetos\crypto\ETL\GCP.json' # Windows
    path_json ='/mnt/c/projetos/crypto/ETL/GCP.json' # Linux
    credentials = service_account.Credentials.from_service_account_file(path_json)
    # Enviando os dados 
    pandas_gbq.to_gbq(df,destination_table=f'{dataset}.{table}',project_id=project_id,if_exists=if_exists,credentials=credentials)
    return print('Processo de ETL da tabela {} concluído!\n\n'.format(table))


# Função de nomear as tabelas em função da crypto
def name_table(lista_crypto):
    lista_table = []
    for i in lista_crypto:
        lista_table.append('{}_table'.format(i))
    return lista_table



