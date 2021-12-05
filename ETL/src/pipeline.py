from config import LIST_CRIPTO
from loading import Loading
from extract import Extract


class Pipeline:
    def __init__(self,pipeline_init,pipeline_update) -> None:
        self.pipeline_init = pipeline_init
        self.pipeline_update = pipeline_update
        pass
    def pipeline_init(self,database = 'bigquery'):
        """Pipeline para inserção inicial dos dados.\n
        Database = 'bigquery' or 'mysql' """
        for i in range(len(LIST_CRIPTO)):
            df = Extract.extract_binance(LIST_CRIPTO[i])
            if database == 'bigquery':
                Loading().BigQuery(df,if_exists='replace')
            elif database == 'mysql':
                Loading().MySQL(df,LIST_CRIPTO[i])
            else:
                NameError.args('Erro no nome da base de dados para o carregamento')
        return print('\nProcesso de ETL completo para as seguintes criptomoedas:\n',LIST_CRIPTO)
    
    def pipeline_update(self, database = str):
        for i in range(len(LIST_CRIPTO)):

            Date = '1 Jan, 2019' # Pegar a útima data do logging info
            df = Extract.extract_binance(LIST_CRIPTO[i],date=f'{Date}')
            df = Extract.extract_binance(LIST_CRIPTO[i])
            if database == 'bigquery':
                Loading().BigQuery(df,table=LIST_CRIPTO[i],if_exists='append')
            elif database == 'mysql':
                Loading().MySQL(df,LIST_CRIPTO[i],if_exists='append')
        return print('\nProcesso de ETL completo para as seguintes criptomoedas:\n',LIST_CRIPTO)


#if __name__ == '__main__':
    #pipeline()

    



