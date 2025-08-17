import pandas as pd
import numpy as np

def vendas_por_data_pedido(df: pd.DataFrame) -> pd.DataFrame:
    """Calcula o total de vendas por data do pedido."""
    df_result = df.groupby('Data_Pedido')['Valor_Venda'].sum()
    return df_result.reset_index()

def vendas_por_estado(df: pd.DataFrame) -> pd.DataFrame:
    """Calcula o total de vendas por estado."""
    df_result = df.groupby('Estado')['Valor_Venda'].sum().reset_index()
    return df_result

def top_10_cidades(df: pd.DataFrame) -> pd.DataFrame:
    """Identifica as 10 cidades com maior total de vendas."""
    df_result = df.groupby('Cidade')['Valor_Venda'].sum().reset_index().sort_values(
        by='Valor_Venda', ascending=False
    ).head(10)
    return df_result

def vendas_por_segmento(df: pd.DataFrame) -> pd.DataFrame:
    """Calcula o total de vendas por segmento."""
    df_result = df.groupby('Segmento')['Valor_Venda'].sum().reset_index().sort_values(
        by='Valor_Venda', ascending=False
    )
    return df_result

def vendas_por_segmento_ano_mes(df: pd.DataFrame) -> pd.DataFrame:
    """Calcula a média de vendas por segmento, ano e mês."""
    df['Ano'] = df['Data_Pedido'].dt.year
    df['Mes'] = df['Data_Pedido'].dt.month
    df_result = df.groupby(['Ano', 'Mes', 'Segmento'])['Valor_Venda'].agg([np.mean]).reset_index()
    return df_result

def top_12_subcategorias(df: pd.DataFrame) -> pd.DataFrame:
    """Identifica as top 12 subcategorias por vendas."""
    df_result = df.groupby(['Categoria', 'SubCategoria']).sum(numeric_only=True).sort_values(
        'Valor_Venda', ascending=False
    ).head(12).reset_index()
    return df_result