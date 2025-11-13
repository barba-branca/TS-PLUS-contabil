# Automação de Lançamentos Contábeis via TSPlus

Este projeto automatiza o processo de lançamento de dados de uma planilha Excel em um sistema de contabilidade acessado via TSPlus HTML5 Remote Desktop.

## Objetivo

O objetivo principal é eliminar a tarefa manual e repetitiva de digitar dados de uma planilha (`dados.xlsx`) no sistema contábil remoto. O robô realiza o processo completo, desde o login no portal até a navegação e o lançamento de cada registro.

## Como Funciona

A automação é construída em Python e utiliza a biblioteca **Selenium** para controlar o navegador Google Chrome.

O fluxo de execução é o seguinte:
1.  **Login HTML**: Acessa a URL do TSPlus e preenche os campos de usuário e senha na tela de login padrão.
2.  **Interação com Canvas**: Após o login, o sistema remoto é renderizado dentro de um elemento `<canvas>` HTML5. Todas as interações a partir deste ponto (cliques e digitação) são feitas calculando as coordenadas (X, Y) dentro deste canvas.
3.  **Navegação no Sistema**: O robô clica em menus para abrir o módulo contábil e a tela de lançamentos.
4.  **Leitura da Planilha**: Os dados de lançamento são lidos do arquivo `dados.xlsx`.
5.  **Lançamento Automático**: Cada linha da planilha é lida e digitada nos campos correspondentes da tela do sistema.

## Estrutura do Projeto

```
automacao_tsplus/
│
├── main.py           # Orquestra o fluxo principal da automação
├── actions.py        # Contém as funções de interação (cliques, digitação)
├── config.py         # Arquivo de configuração (URLs, senhas, coordenadas)
├── excel_utils.py    # Utilitário para ler a planilha Excel
├── dados.xlsx        # Planilha com os dados a serem lançados
└── README.md         # Este arquivo
```

## Pré-requisitos

Para executar este projeto, você precisa ter o Python 3 instalado, juntamente com o gerenciador de pacotes `pip`.

1.  **Instale as bibliotecas necessárias**:
    Abra um terminal ou prompt de comando e execute o seguinte comando para instalar as dependências:
    ```bash
    pip install pandas openpyxl selenium webdriver-manager
    ```

## Configuração

Antes de executar, você precisa ajustar o arquivo `config.py` com as suas informações:

1.  **Credenciais**:
    - `USUARIO_TSPLUS` e `SENHA_TSPLUS`: Suas credenciais para o login web.
    - `USUARIO_WINDOWS` e `SENHA_WINDOWS`: Suas credenciais para o login no Windows remoto.

2.  **Coordenadas**:
    - As coordenadas no arquivo `config.py` são apenas exemplos. **É muito provável que você precise ajustá-las** para que correspondam à sua resolução de tela e ao layout do sistema. Use uma ferramenta de captura de coordenadas (como o Paint ou aplicativos específicos) para encontrar os valores corretos para cada elemento (campos de usuário/senha, menus, etc.).

## Como Executar

1.  **Preencha a planilha `dados.xlsx`** com os dados que você deseja lançar. Mantenha as colunas `data`, `debitar` e `creditar`.
2.  **Ajuste o arquivo `config.py`** conforme descrito na seção de configuração.
3.  **Execute o script principal**:
    Navegue até a pasta do projeto no seu terminal e execute:
    ```bash
    python automacao_tsplus/main.py
    ```

O robô iniciará o navegador Chrome, executará todo o processo e exibirá o progresso no terminal.
