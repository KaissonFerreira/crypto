from ETL.src.pipeline import Pipeline
from pipeline import Pipeline as pp

if __name__ == '__main__':
# Inicializando o pipeline de inicio
    pp.pipeline_init(Pipeline,database='bigquery')

# Pipeline para update
    #pp.Pipeline().pipeline_update()

