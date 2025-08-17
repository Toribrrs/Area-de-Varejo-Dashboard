import pandas as pd

def clean_data(df):
    """Limpeza básica do DataFrame."""
    df = df.dropna()
    df = df.drop_duplicates()
    return df

def add_features(df):
    """Adiciona features como ano, mês, etc."""
    df['Ano'] = df['Data_Pedido'].dt.year
    df['Mes'] = df['Data_Pedido'].dt.month
    return df