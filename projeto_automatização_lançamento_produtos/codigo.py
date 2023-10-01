# passo a passo do projeto
"""
passo 1: Entrar no sistema da empresa https://dlp.hashtagtreinamentos.com/python/intensivao/login
passo 2: Fazer login
passo 3: Importar a base de produtos
passo 4: Cadastrar um produto
passo 5: Repetir o cadastro para todos os produtos
"""
    
import pyautogui
import time
#pyautogui.click -> CLICAR COM O MOUSE
#pyautogui.write -> ESCREVER TEXTO
#pyautogui.press -> APERTAR 1 TECLA
#pyautogui.hotkey -> ATALHO (COMBNAÇÃO DE TECLAS)

pyautogui.PAUSE = 0.8


pyautogui.press('win')
pyautogui.write('opera')
pyautogui.press('enter')

link = 'https://dlp.hashtagtreinamentos.com/python/intensivao/login'

time.sleep(1)

pyautogui.write(link)
pyautogui.press("enter")

time.sleep(3)

pyautogui.click(x=546, y=390)
pyautogui.write('hemo.gestor3')
pyautogui.click(x=548, y=487)
pyautogui.write('102030402023')

pyautogui.press('enter')

time.sleep(2)

import pandas

tabela = pandas.read_csv("produtos.csv")

for linha in tabela.index:
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'codigo']))
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'marca']))
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'tipo']))
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'categoria']))
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'preco_unitario']))
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'custo']))
    pyautogui.press('tab')

    obs = tabela.loc[linha, 'obs']
    if not pandas.isna(obs):
        pyautogui.write(str(obs))



    pyautogui.press('tab')
    pyautogui.press('enter')
    pyautogui.scroll(50000)
    pyautogui.click(x=237, y=234)




