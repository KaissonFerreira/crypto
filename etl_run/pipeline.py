from config import LIST_CRIPTO
from loading import Loading
from extract import Extract


def pipeline():
    for i in range(len(LIST_CRIPTO)):
        df = Extract.extract_binance(LIST_CRIPTO[i])
        Loading().BigQuery(df)
    print('\nProcesso de ETL completo para as seguintes criptomoedas')
    return print(LIST_CRIPTO)


if __name__ == '__main__':
    pipeline()

    



