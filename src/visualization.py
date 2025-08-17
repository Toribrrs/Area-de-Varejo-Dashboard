 # Funções de gráficos
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

def plot_hist(df: pd.DataFrame, column: str):
    if pd.api.types.is_numeric_dtype(df[column]):
        fig, ax = plt.subplots(figsize=(6, 4))
        sns.histplot(df[column], bins=20, kde=True, ax=ax)
        ax.set_title(f"Distribuição de {column}")
        return fig
    else:
        return None

def plot_correlation(df: pd.DataFrame):
    num_cols = df.select_dtypes(include=['number']).columns
    if len(num_cols) >= 2:
        corr_matrix = df[num_cols].corr(numeric_only=True)
        fig, ax = plt.subplots(figsize=(8, 6))
        sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", ax=ax)
        ax.set_title("Matriz de Correlação")
        return fig
    else:
        return None


def plot_vendas_por_data(df: pd.DataFrame):
    """Gera o gráfico de linha de vendas por data."""
    fig, ax = plt.subplots(figsize=(20, 6))
    df.plot(y='Valor_Venda', color='green', ax=ax)
    ax.set_title('Total de Vendas Por Data do Pedido')
    ax.set_xlabel('Data Pedido')
    ax.set_ylabel('Valor de Venda')
    return fig

def plot_vendas_por_estado(df: pd.DataFrame):
    """Gera o gráfico de barras de vendas por estado."""
    fig, ax = plt.subplots(figsize=(16, 6))
    sns.barplot(data=df, y='Valor_Venda', x='Estado', ax=ax)
    ax.set_title('Vendas Por Estado')
    plt.xticks(rotation=80)
    return fig

def plot_top_10_cidades(df: pd.DataFrame):
    """Gera o gráfico de barras das top 10 cidades."""
    fig, ax = plt.subplots(figsize=(16, 6))
    sns.set_palette('coolwarm')
    sns.barplot(data=df, y='Valor_Venda', x='Cidade', ax=ax)
    ax.set_title('As 10 Cidades com Maior Total de Vendas')
    return fig

def plot_vendas_por_segmento_pizza(df: pd.DataFrame):
    """Gera o gráfico de pizza de vendas por segmento."""
    def autopct_format(values):
        def my_format(pct):
            total = sum(values)
            val = int(round(pct * total / 100.0))
            return '$ {v:d}'.format(v=val)
        return my_format

    fig, ax = plt.subplots(figsize=(10, 6))
    plt.pie(
        df['Valor_Venda'], 
        labels=df['Segmento'],
        autopct=autopct_format(df['Valor_Venda']),
        startangle=90
    )
    centre_circle = plt.Circle((0, 0), 0.82, fc='white')
    ax.add_artist(centre_circle)
    ax.annotate(text='Total de Vendas: ' + '$ ' + str(int(sum(df['Valor_Venda']))), xy=(-0.25, 0))
    ax.set_title('Total de Vendas Por Segmento')
    return fig

def plot_vendas_por_segmento_ano_mes(df: pd.DataFrame):
    """Gera o gráfico de linha de vendas por segmento, ano e mês."""
    fig = sns.relplot(
        kind='line',
        data=df,
        y='mean',
        x='Mes',
        hue='Segmento',
        col='Ano',
        col_wrap=4
    )
    fig.set_titles("Ano: {col_name}")
    return fig