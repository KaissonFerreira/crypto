from extract.config import extract_binance,name_table,update_bq


# Lista de criptomoedas que serão avaliadas...
lista_crypto = ['DOT', 
                'MATIC', 
                'SOL', 
                'BTT',
                'ADA', 
                'BTC', 
                'ETH']

lista_table = name_table(lista_crypto)
def etl():
    for i in range(len(lista_crypto)):
        df = extract_binance(lista_crypto[i])
        update_bq(df,lista_table[i])
    print('\nProcesso de ETL completo para as seguintes criptomoedas')
    return print(lista_crypto)


if __name__ == '__main__':
    etl()

    



