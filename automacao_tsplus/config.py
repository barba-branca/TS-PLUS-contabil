# -*- coding: utf-8 -*-

"""
Arquivo de configuração para a automação TSPlus.
"""

# URL do TSPlus
TSPLUS_URL = "https://ts-plusx1.kblcontabilidade.com.br/software/html5.html"

# Credenciais de login do TSPlus (tela HTML)
USUARIO_TSPLUS = "kaue.martins"
SENHA_TSPLUS = "JXX#c0W4"

# Credenciais de login do Windows (dentro do canvas)
USUARIO_WINDOWS = "seu_usuario_windows"
SENHA_WINDOWS = "sua_senha_windows"

# Coordenadas para o login do Windows no canvas
COORD_LOGIN_USUARIO = (982, 452)
COORD_LOGIN_SENHA = (982, 482)
COORD_LOGIN_OK = (995, 569)

# Coordenadas para a navegação nos menus do sistema
COORD_MENU_DOMINIO = (69, 151)
COORD_MENU_CONTABIL = (58, 379)
COORD_MENU_MOVIMENTOS = (153, 458)
COORD_MENU_CONSULTA = (321, 145)

# Coordenadas para a tela de lançamento
COORD_CAMPO_DATA = (355, 193)
COORD_DATA_HOJE = (1164, 647)

# Tempos de espera (em segundos)
WAIT_TIME_SHORT = 2
WAIT_TIME_MEDIUM = 5
WAIT_TIME_LONG = 10
WAIT_FOR_CANVAS = 20
