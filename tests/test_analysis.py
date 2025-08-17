 # Testes unitários

import pandas as pd
import pytest
from src.analysis import vendas_por_estado, top_10_cidades

@pytest.fixture
def sample_data():
    """Retorna um DataFrame de exemplo para testes."""
    data = {
        'Estado': ['SP', 'RJ', 'SP', 'RJ', 'MG'],
        'Valor_Venda': [100, 200, 150, 300, 50]
    }
    return pd.DataFrame(data)

def test_vendas_por_estado(sample_data):
    """Testa se a função vendas_por_estado calcula corretamente."""
    # Chama a função com os dados de exemplo
    result_df = vendas_por_estado(sample_data)
    
    # Define o resultado esperado
    expected_data = {
        'Estado': ['MG', 'RJ', 'SP'],
        'Valor_Venda': [50, 500, 250]
    }
    expected_df = pd.DataFrame(expected_data)
    
    # Compara o resultado obtido com o resultado esperado
    pd.testing.assert_frame_equal(
        result_df.sort_values(by='Estado').reset_index(drop=True), 
        expected_df.sort_values(by='Estado').reset_index(drop=True)
    )

def test_top_10_cidades():
    """Testa se a função top_10_cidades retorna as 10 maiores vendas."""
    # Cria um DataFrame de exemplo com mais de 10 cidades
    data = {
        'Cidade': [f'Cidade{i}' for i in range(20)],
        'Valor_Venda': range(20, 0, -1) # Valores de 20 a 1 em ordem decrescente
    }
    df = pd.DataFrame(data)
    
    # Chama a função
    result_df = top_10_cidades(df)
    
    # Verifica se o resultado tem 10 linhas
    assert len(result_df) == 10
    
    # Verifica se a cidade com maior valor está na primeira posição
    assert result_df.iloc[0]['Cidade'] == 'Cidade0'