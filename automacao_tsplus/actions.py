# -*- coding: utf-8 -*-

"""
Módulo com as ações de automação para a interface TSPlus.

Contém funções de baixo nível para interagir com o canvas e funções
de alto nível que orquestram o fluxo de login e navegação no sistema.
"""

import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import config

# --- Funções de Baixo Nível (Interação com Canvas) ---

def click_canvas(driver, x, y):
    """
    Clica em uma coordenada específica (x, y) dentro do elemento canvas.

    Args:
        driver: A instância do WebDriver do Selenium.
        x (int): A coordenada X para o clique.
        y (int): A coordenada Y para o clique.
    """
    try:
        canvas = driver.find_element(By.TAG_NAME, "canvas")
        action = ActionChains(driver)
        action.move_to_element_with_offset(canvas, x, y).click().perform()
        print(f"Canvas clicado nas coordenadas: ({x}, {y})")
        time.sleep(config.WAIT_TIME_SHORT)  # Espera para a ação ser processada
    except Exception as e:
        print(f"Erro ao clicar no canvas: {e}")

def send_keys_canvas(driver, text):
    """
    Envia uma sequência de teclas para o canvas.

    Args:
        driver: A instância do WebDriver do Selenium.
        text (str): O texto a ser enviado.
    """
    try:
        canvas = driver.find_element(By.TAG_NAME, "canvas")
        action = ActionChains(driver)
        action.move_to_element(canvas).send_keys(text).perform()
        print(f"Texto enviado para o canvas: '{text}'")
        time.sleep(config.WAIT_TIME_SHORT)
    except Exception as e:
        print(f"Erro ao enviar texto para o canvas: {e}")

def send_enter(driver):
    """Envia a tecla ENTER para o elemento ativo (esperado que seja o canvas)."""
    try:
        action = ActionChains(driver)
        action.send_keys(Keys.ENTER).perform()
        print("Tecla ENTER enviada.")
        time.sleep(config.WAIT_TIME_SHORT)
    except Exception as e:
        print(f"Erro ao enviar a tecla ENTER: {e}")

def send_tab(driver):
    """Envia a tecla TAB para o elemento ativo (esperado que seja o canvas)."""
    try:
        action = ActionChains(driver)
        action.send_keys(Keys.TAB).perform()
        print("Tecla TAB enviada.")
        time.sleep(config.WAIT_TIME_SHORT)
    except Exception as e:
        print(f"Erro ao enviar a tecla TAB: {e}")


# --- Funções de Alto Nível (Fluxo de Automação) ---

def login_html(driver):
    """
    Executa o login na tela inicial HTML do TSPlus.
    """
    try:
        driver.get(config.TSPLUS_URL)
        print("Acessando a URL do TSPlus.")

        # Aguarda os campos de login estarem presentes
        wait = WebDriverWait(driver, config.WAIT_TIME_MEDIUM)

        username_field = wait.until(EC.presence_of_element_located((By.ID, "Editbox1")))
        password_field = driver.find_element(By.ID, "Editbox2")
        login_button = driver.find_element(By.ID, "buttonLogOn")

        username_field.send_keys(config.USUARIO_TSPLUS)
        password_field.send_keys(config.SENHA_TSPLUS)
        print("Credenciais HTML inseridas.")

        login_button.click()
        print("Botão de login HTML clicado.")

        # Aguarda o canvas aparecer após o login
        print(f"Aguardando o canvas carregar por {config.WAIT_FOR_CANVAS} segundos...")
        wait = WebDriverWait(driver, config.WAIT_FOR_CANVAS)
        wait.until(EC.presence_of_element_located((By.TAG_NAME, "canvas")))
        print("Canvas carregado com sucesso.")

    except Exception as e:
        print(f"Erro durante o login HTML: {e}")
        driver.quit()

def login_windows(driver):
    """
    Executa o login na tela do Windows dentro do canvas.
    """
    print("Iniciando login no Windows via canvas...")
    time.sleep(config.WAIT_TIME_MEDIUM) # Espera extra para a tela do Windows estabilizar

    # Inserir usuário do Windows
    click_canvas(driver, *config.COORD_LOGIN_USUARIO)
    send_keys_canvas(driver, config.USUARIO_WINDOWS)

    # Inserir senha do Windows
    click_canvas(driver, *config.COORD_LOGIN_SENHA)
    send_keys_canvas(driver, config.SENHA_WINDOWS)

    # Clicar em OK
    click_canvas(driver, *config.COORD_LOGIN_OK)
    print("Login no Windows finalizado.")
    time.sleep(config.WAIT_TIME_LONG) # Espera para o desktop carregar

def abrir_modulo_contabil(driver):
    """
    Navega pelos menus para abrir o módulo contábil.
    """
    print("Abrindo módulo contábil...")
    click_canvas(driver, *config.COORD_MENU_DOMINIO)
    click_canvas(driver, *config.COORD_MENU_CONTABIL)
    print("Módulo contábil aberto.")
    time.sleep(config.WAIT_TIME_MEDIUM)

def abrir_tela_movimentos(driver):
    """
    Navega pelos menus para abrir a tela de consulta de movimentos.
    """
    print("Abrindo tela de movimentos...")
    click_canvas(driver, *config.COORD_MENU_MOVIMENTOS)
    click_canvas(driver, *config.COORD_MENU_CONSULTA)
    print("Tela de consulta de movimentos aberta.")
    time.sleep(config.WAIT_TIME_MEDIUM)

def lancar_movimento(driver, data, debitar, creditar):
    """
    Lança um único movimento na tela do sistema.
    Esta é uma função de exemplo e precisa ser adaptada para a tela real.
    """
    print(f"Iniciando lançamento: Data={data}, Débito={debitar}, Crédito={creditar}")

    # Exemplo de sequência de lançamento:
    # 1. Clica no campo de data
    click_canvas(driver, *config.COORD_CAMPO_DATA)

    # 2. Insere a data
    send_keys_canvas(driver, str(data))
    send_tab(driver) # Pula para o próximo campo

    # 3. Insere o valor a debitar
    send_keys_canvas(driver, str(debitar))
    send_tab(driver)

    # 4. Insere o valor a creditar
    send_keys_canvas(driver, str(creditar))
    send_enter(driver) # Confirma o lançamento

    print("Lançamento finalizado.")
    time.sleep(config.WAIT_TIME_SHORT)
