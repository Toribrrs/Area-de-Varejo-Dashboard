# 📊 Data Science Dashboard - Área de Varejo

Um dashboard interativo construído com Streamlit para análise de dados de varejo. O aplicativo carrega, processa e visualiza um conjunto de dados de vendas, oferecendo insights sobre o desempenho em diferentes categorias, estados e segmentos.

## 🚀 Funcionalidades

-   **Visão Geral:** Exibe uma amostra dos dados e gráficos de vendas por estado, top 10 cidades e total por segmento.
-   **Análise de Distribuição:** Permite explorar a distribuição de colunas numéricas através de histogramas interativos.
-   **Outros Gráficos:** Apresenta gráficos adicionais como total de vendas por data do pedido e a média de vendas por segmento ao longo do tempo.
-   **Relatório de Dados:** Gera um relatório de perfil de dados em tempo real, exibindo informações estatísticas, estatísticas descritivas e contagens de valores ausentes.

## 📁 Estrutura do Projeto
---

## 🚀 Estrutura

├── app.py
├── data/
│   └── dataset.csv
├── src/
│   ├── analysis.py
│   ├── data_loader.py
│   ├── data_processing.py
│   ├── reporting.py
│   └── visualization.py
├── tests/
├── requirements.txt
└── README.md
--- 

## 🛠️ Instalação

Certifique-se de ter o Python instalado (versão 3.8 ou superior).

1.  Clone o repositório ou baixe os arquivos.
2.  Navegue até o diretório do projeto no terminal.
3.  Instale as dependências usando o `pip`:

    ```bash
    pip install -r requirements.txt
    ```

## ▶️ Como Rodar

Após a instalação, execute o seguinte comando no terminal para iniciar o aplicativo:

```bash
python -m streamlit run app.py
