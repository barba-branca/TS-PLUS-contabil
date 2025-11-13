# -*- coding: utf-8 -*-

"""
Utilitários para manipulação de planilhas Excel.
"""

import pandas as pd

def carregar_lancamentos(caminho_arquivo):
    """
    Carrega os dados de lançamento de uma planilha Excel.

    Args:
        caminho_arquivo (str): O caminho para o arquivo .xlsx.

    Returns:
        list: Uma lista de dicionários, onde cada dicionário representa uma linha
              da planilha com as colunas 'data', 'debitar' e 'creditar'.
              Retorna uma lista vazia se o arquivo não for encontrado ou ocorrer um erro.
    """
    try:
        df = pd.read_excel(caminho_arquivo)
        # Converte o DataFrame para uma lista de dicionários
        return df.to_dict('records')
    except FileNotFoundError:
        print(f"Erro: O arquivo '{caminho_arquivo}' não foi encontrado.")
        return []
    except Exception as e:
        print(f"Ocorreu um erro ao ler a planilha: {e}")
        return []

if __name__ == '__main__':
    # Exemplo de uso
    lancamentos = carregar_lancamentos('dados.xlsx')
    if lancamentos:
        for lancamento in lancamentos:
            print(lancamento)
