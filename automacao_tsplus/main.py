# -*- coding: utf-8 -*-

"""
Script principal para a automação do TSPlus.

Este script executa o fluxo completo:
1. Inicia o WebDriver do Chrome.
2. Realiza o login na página HTML do TSPlus.
3. Realiza o login no ambiente Windows dentro do canvas.
4. Navega pelos menus para abrir a tela de lançamento.
5. Carrega os dados de uma planilha Excel.
6. Itera sobre os dados e os lança no sistema.
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import actions
import excel_utils
import config

def main():
    """
    Função principal que orquestra a automação.
    """
    # Instala e configura o ChromeDriver automaticamente
    service = ChromeService(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    try:
        # Etapa 1: Login na interface HTML
        actions.login_html(driver)

        # Etapa 2: Login no Windows (dentro do canvas)
        actions.login_windows(driver)

        # Etapa 3: Abrir o módulo contábil
        actions.abrir_modulo_contabil(driver)

        # Etapa 4: Abrir a tela de movimentos
        actions.abrir_tela_movimentos(driver)

        # Etapa 5: Carregar dados da planilha
        caminho_planilha = 'dados.xlsx'
        lancamentos = excel_utils.carregar_lancamentos(caminho_planilha)

        if not lancamentos:
            print("Nenhum dado para lançar. Verifique a planilha.")
            return

        # Etapa 6: Loop de lançamento dos dados
        print(f"Iniciando o lançamento de {len(lancamentos)} registros...")
        for lancamento in lancamentos:
            actions.lancar_movimento(
                driver,
                data=lancamento['data'],
                debitar=lancamento['debitar'],
                creditar=lancamento['creditar']
            )

        print("Todos os lançamentos foram concluídos com sucesso!")

    except Exception as e:
        print(f"Ocorreu um erro inesperado no fluxo principal: {e}")
    finally:
        # Garante que o navegador seja fechado ao final
        print("Fechando o navegador...")
        driver.quit()

if __name__ == "__main__":
    # Instala o webdriver-manager para gerenciar o chromedriver
    import subprocess
    import sys
    try:
        import webdriver_manager
    except ImportError:
        print("Instalando webdriver-manager...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "webdriver-manager"])
        print("webdriver-manager instalado com sucesso.")

    main()
