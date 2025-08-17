import pandas as pd
import streamlit as st

def gerar_relatorio(df: pd.DataFrame):
    """Exibe um relatório de análise de dados exploratória no Streamlit."""
    
    # Exibe estatísticas descritivas
    st.subheader("Estatísticas Descritivas")
    st.dataframe(df.describe())
    
    # Exibe valores ausentes por coluna
    st.subheader("Valores Ausentes por Coluna")
    missing_values = df.isnull().sum()
    st.dataframe(missing_values)