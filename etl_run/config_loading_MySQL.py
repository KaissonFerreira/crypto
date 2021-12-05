#%%
import mysql.connector
import os
import pandas as pd
from config_extract import Extract

# Lista de criptomoedas que serão avaliadas...
lista_crypto = ['DOT', 
                'MATIC', 
                'SOL', 
                'BTT',
                'ADA', 
                'BTC', 
                'ETH']

#%%
#def update_bd_mysql(df, table):
    #"""Função utilizada para inserção dos dados no banco de dados Mysql"""
# Iniciando a conexão com o banco de dados MySQL

conn = mysql.connector.connect(user='root', password=os.environ['SENHA'],
                                host='127.0.0.1',
                                database='crypto-project')
# Verificando o status de conexão
if conn.is_connected():
    db_info = conn.get_server_info()
    print("Conectado ao servidor MySQL versão",db_info)
    cursor = conn.cursor()
    cursor.execute("select database();")
    linha = cursor.fetchone()
    print("Conectado ao banco de dados",linha)
#%%
pd.read_sql('select * from crypto_table',conn)

#%%
df = Extract("ETH")
df = df.extract_binance()
df.to_sql('name = ETH',conn)
    
#%%
# Terminando a conexão com o banco de dados
if conn.is_connected():
    cursor.close()
    conn.close()
    print("A conexão com MySQL foi encerrada!")
