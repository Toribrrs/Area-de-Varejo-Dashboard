import pandas as pd

def load_data(path: str) -> pd.DataFrame:
    """Carrega o dataset e ajusta tipos de dados."""
    df = pd.read_csv(path)
    df['Data_Pedido'] = pd.to_datetime(df['Data_Pedido'], format='%d/%m/%Y')
    return df