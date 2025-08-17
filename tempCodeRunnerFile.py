import streamlit as st
import pandas as pd
from src.db_utils import run_query
from src.data_processing import clean_data, add_features
from src.visualization import plot_hist, plot_correlation
import matplotlib.pyplot as plt

st.set_page_config(page_title="Data Science Dashboard", layout="wide")

st.title("📊 Data Science Dashboard")
st.sidebar.header("Configurações")

# Input SQL
query = st.sidebar.text_area("Escreva sua query SQL:", "SELECT * FROM tabela;")

if st.sidebar.button("Executar"):
    try:
        df = run_query(query)
        st.subheader("📋 Resultados da Query")
        st.dataframe(df)

        # Processamento
        df = clean_data(df)
        df = add_features(df)

        # Visualizações
        st.subheader("📈 Visualizações")
        col1, col2 = st.columns(2)

        if not df.empty:
            with col1:
                num_cols = df.select_dtypes(include=["int64","float64"]).columns.tolist()
                if num_cols:
                    col_selected = st.selectbox("Escolha uma coluna numérica:", num_cols)
                    fig, ax = plt.subplots()
                    plot_hist(df, col_selected)
                    st.pyplot(fig)

            with col2:
                fig, ax = plt.subplots()
                plot_correlation(df)
                st.pyplot(fig)

    except Exception as e:
        st.error(f"Erro ao executar query: {e}")
