# Passo a passo do projeto
# Passo 1 - Entrar no sistema da empresa
        # # https://dlp.hashtagtreinamentos.com/python/intensivao/login
    # clicar -> pyautogui.click
    # escrever -> pyautogui.write
    # apertar uma tecla -> pyautogui.press
    # apertar -> pyautogui.hotkey
    # scroll -> pyautogui.scroll
# Passo 2 - Fazer Login
# Passo 3 - Importar a base de dados
# Passo 4 - Cadastrar um produtominha senhaLogitech25.95    6.5     
# Passo 5 - Repetir isso até acabar a base de dados

import pyautogui
import time
pyautogui.PAUSE = 1
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("enter")
time.sleep(5)
pyautogui.click(x=7331, y=620)
email = "pythonimpressionador@gmail.com"
pyautogui.write(email)
pyautogui.press("tab")
pyautogui.write("minha senha")
pyautogui.click(x=7655, y=861)

import pandas
tabela = pandas.read_csv("produtos.csv")
print(tabela)

for linha in tabela.index:
    pyautogui.click(x=7322, y=438)
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(codigo)
    pyautogui.press("tab")
    marca = tabela.loc[linha, "marca"]
    pyautogui.write("marca")
    pyautogui.press("tab")
    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write("tipo")
    pyautogui.press("tab")
    categoria = tabela.loc[linha, "categoria"]
    pyautogui.write("categoria")
    pyautogui.press("tab")
    preco_unitario = tabela.loc[linha, "preco_unitario"]
    pyautogui.write("preco_unitario")
    pyautogui.press("tab")
    custo = tabela.loc[linha, "custo"]
    pyautogui.write("custo")
    pyautogui.press("tab")
    obs = tabela.loc[linha, "obs"]
    pyautogui.write("obs")
    pyautogui.press("tab")
    pyautogui.press("enter")

    pyautogui.scroll(5000)
