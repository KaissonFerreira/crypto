import config
from loading import Loading
from extract import Extract

class Pipeline:
    lista_cripto = config.LIST_CRIPTO
    def __init__(self, lista_cripto = lista_cripto):
        self.lista_cripto = lista_cripto
        

    def pipeline_init(self,database = str):
        """Pipeline para inserção inicial dos dados.\n
        Database = 'bigquery' or 'mysql' """ 

        cripto = self.lista_cripto
        for i in range(len(cripto)):
            df = Extract.extract_binance(symbol=list(cripto)[i])
            if database == 'bigquery':
                Loading().BigQuery(df,table=list(cripto.values())[i],if_exists='replace')
            elif database == 'mysql':
                Loading().MySQL(df,cripto[i])
            else:
                NameError.args('Erro no nome da base de dados para o carregamento')
        return print('\nProcesso de ETL completo para as seguintes criptomoedas:\n',list(cripto))
    
    def pipeline_update(self, database = str):
        cripto = self.cripto
        for i in range(len(cripto)):

            Date = '1 Jan, 2019' # Pegar a útima data do logging info
            df = Extract.extract_binance(cripto[i],date=f'{Date}')
            df = Extract.extract_binance(cripto[i])
            if database == 'bigquery':
                Loading().BigQuery(df,table=cripto[i],if_exists='append')
            elif database == 'mysql':
                Loading().MySQL(df,cripto[i],if_exists='append')
        return print('\nProcesso de ETL completo para as seguintes criptomoedas:\n',list(cripto))


if __name__ == '__main__':
    Pipeline.pipeline_init(Pipeline,database='bigquery')

    



