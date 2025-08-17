import streamlit as st
import pandas as pd
from src.data_loader import load_data
from src.data_processing import clean_data, add_features
from src.analysis import (
    vendas_por_data_pedido,
    vendas_por_estado,
    top_10_cidades,
    vendas_por_segmento,
    vendas_por_segmento_ano_mes,
)
from src.visualization import (
    plot_hist,
    plot_vendas_por_data,
    plot_vendas_por_estado,
    plot_top_10_cidades,
    plot_vendas_por_segmento_pizza,
    plot_vendas_por_segmento_ano_mes
)
from src.reporting import gerar_relatorio

st.set_page_config(page_title="Data Science Dashboard", layout="wide")

st.title("📊 Análise de Dados de Varejo")

@st.cache_data
def get_data():
    try:
        df = load_data("data/dataset.csv")
        df = clean_data(df)
        df = add_features(df)
        return df
    except FileNotFoundError:
        st.error("Erro: O arquivo 'data/dataset.csv' não foi encontrado.")
        return None

df = get_data()

if df is None:
    st.warning("Verifique se o arquivo 'dataset.csv' está na pasta 'data'.")
    st.stop()

st.sidebar.title("Menu de Navegação")
menu_selection = st.sidebar.radio(
    "Escolha uma página:",
    ["Visão Geral", "Análise de Distribuição", "Outros Gráficos", "Relatório de Dados"]
)

if menu_selection == "Visão Geral":
    st.header("Visão Geral do Dataset")
    st.markdown("Uma breve análise dos dados mais importantes do seu conjunto de dados de varejo.")

    with st.expander("Ver amostra dos dados"):
        st.dataframe(df.head(10))

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Vendas Por Estado")
        df_vendas_estado = vendas_por_estado(df)
        fig_estado = plot_vendas_por_estado(df_vendas_estado)
        st.pyplot(fig_estado)

    with col2:
        st.subheader("Top 10 Cidades com Maior Venda")
        df_top_cidades = top_10_cidades(df)
        fig_cidades = plot_top_10_cidades(df_top_cidades)
        st.pyplot(fig_cidades)

    st.subheader("Total de Vendas Por Segmento")
    df_vendas_segmento = vendas_por_segmento(df)
    fig_segmento_pizza = plot_vendas_por_segmento_pizza(df_vendas_segmento)
    st.pyplot(fig_segmento_pizza)
    
elif menu_selection == "Análise de Distribuição":
    st.header("Análise de Distribuição")
    st.markdown("Use o menu ao lado para explorar a distribuição de colunas numéricas.")
    
    st.sidebar.subheader("Opções de Histograma")
    num_cols = df.select_dtypes(include=['number']).columns.tolist()
    if 'Valor_Venda' in num_cols:
        num_cols.remove('Valor_Venda')
        num_cols.insert(0, 'Valor_Venda')
    
    col_selected = st.sidebar.selectbox(
        "Selecione uma coluna para o histograma:",
        num_cols,
        key="hist_col"
    )
    
    if col_selected:
        fig_hist = plot_hist(df, col_selected)
        st.subheader(f"Distribuição de {col_selected}")
        st.pyplot(fig_hist)
    else:
        st.info("Nenhuma coluna numérica disponível para o histograma.")

elif menu_selection == "Outros Gráficos":
    st.header("Outros Gráficos")
    st.markdown("Uma coleção de gráficos adicionais para insights mais profundos.")

    st.subheader("Total de Vendas Por Data do Pedido")
    df_vendas_data = vendas_por_data_pedido(df)
    fig_data = plot_vendas_por_data(df_vendas_data)
    st.pyplot(fig_data)

    st.subheader("Média de Vendas Por Segmento, Ano e Mês")
    df_segmento_ano_mes = vendas_por_segmento_ano_mes(df)
    fig_segmento_ano_mes = plot_vendas_por_segmento_ano_mes(df_segmento_ano_mes)
    st.pyplot(fig_segmento_ano_mes.fig)

elif menu_selection == "Relatório de Dados":
    st.header("Relatório Detalhado do Dataset")
    st.markdown("O relatório abaixo é gerado em tempo real, sem a necessidade de uma biblioteca externa.")

    if st.button("Gerar Relatório de Vendas"):
        with st.spinner('Gerando o relatório...'):
            try:
                gerar_relatorio(df)
                st.success("Relatório exibido com sucesso!")
            except Exception as e:
                st.error(f"Erro ao gerar o relatório: {e}")