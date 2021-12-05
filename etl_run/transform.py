import pandas as pd

class Transform:
    def __init__(self,transform) -> None:
        self.transform = transform
    
    def transform(df):
        df_cripto = pd.DataFrame(df,dtype=float, columns= ('Open_time', 
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
        df_cripto['Open_time'] = pd.to_datetime(df_cripto['Open_time'], unit='ms').dt.tz_localize('UTC').dt.tz_convert('America/Sao_Paulo')
        df_cripto['Close_time'] = pd.to_datetime(df_cripto['Close_time'], unit='ms').dt.tz_localize('UTC').dt.tz_convert('America/Sao_Paulo')

        # Selecionando apenas algumas das colunas
        df_cripto = df_cripto[['Open_time', 
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
        df_cripto['Media_movel'] = df_cripto['Close'].shift(1).rolling(12).mean()
            # Desvio padrão das últimas 12 hrs 
        df_cripto['Desvio_P_12hours'] = df_cripto['Close'].shift(1).rolling(12).std()
            # Banda Inferior
        df_cripto['Banda_inf'] = df_cripto['Media_movel'] - 2*df_cripto['Desvio_P_12hours']
            # Banda Superior
        df_cripto['Banda_sup'] = df_cripto['Media_movel'] + 2*df_cripto['Desvio_P_12hours']

        return df_cripto