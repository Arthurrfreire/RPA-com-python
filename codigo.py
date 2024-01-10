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
    # codigo
    pyautogui.write("MOLO000251")
    pyautogui.press("tab")
    # marca
    pyautogui.write("Logitech")
    pyautogui.press("tab")
    # tipo
    pyautogui.write("Mouse")
    pyautogui.press("tab")
    # categoria
    pyautogui.write("1")
    pyautogui.press("tab")
    # preço
    pyautogui.write("25.95")
    pyautogui.press("tab")
    # custo
    pyautogui.write("6.5")
    pyautogui.press("tab")
    # obs
    pyautogui.write("")
    pyautogui.press("tab")
    pyautogui.press("enter")

    pyautogui.scroll(5000)
