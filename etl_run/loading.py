import pandas_gbq
import config
import mysql.connector as mysql
import sqlalchemy

from google.oauth2 import  service_account


class Loading:
    def __init__(self,BigQuery,MySQL,SQLachemy) -> None:
        self.BigQuery = BigQuery
        self.MySQL = MySQL
        self.SQLachemy = SQLachemy
    
    # Função que envia os dados para o BQ
    def BigQuery(self,dataframe, table, dataset, if_exists = 'replace'):
        """ Essa função envia os dados processados para o Big Query da Google Cloud Plataform.\n
        dataframe = DataFrame que será enviado\n
        table = Nome da tabela\n
        dataset = Nome do Dataset\n
        if_exists = 'append' or 'replace' - default 'replace'\n\n"""
        #print('Inciando o carregamento da tabela {}'.format(table))
        # Conectando com a API
        dataset = config.DATASET
        project_id = config.PROJECT_ID
        path_json = config.CREDENTIALS_GCP
        credentials = service_account.Credentials.from_service_account_file(path_json)
        # Enviando os dados 
        return pandas_gbq.to_gbq(dataframe,destination_table=f'{dataset}.{table}',project_id=project_id,if_exists=if_exists,credentials=credentials)
    
    # Função que envia os dados para o banco de dados do MySQL 
    def MySQL(self,dataframe, table):
        password = config.KEY_SQL
        host = config.HOST
        database = config.DATABASE
        user = config.USER
        conn = mysql.connect(user=user, 
                            password=password,
                            host=host,
                            database=database)

    # Função que envia os dados por meio do SQLAlchemy
    def SQLalchemy (self, dataframe):
        key = config.KEY_SQL
        user = config.USER
        database = config.DATABASE
        engine = sqlalchemy.create_engine(f'mysql+mysqlconnector://{user}:{key}@localhost:3306/{database}')
         