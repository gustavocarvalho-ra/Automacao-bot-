#  {Passo a passo - Criação de um bot para automatizar a inscrição de produtos para a empresa}

# 1- Entrar no sistema da empresa
#      https://dlp.hashtagtreinamentos.com/python/intensivao/tabela

import pyautogui
import time

# pyautogui.click - clicar com o mouse 
# pyautogui.write - escrever um texto
# pyautogui.press - apertar uma tecla
# pyautogui.hotkey - atalho (combinação de teclas)
# time.sleep - dar uma determinada pausa entre as linhas do código

# pyautogui.hotkey("ctrl", "c") - EX de combinação de teclas

# pyautogui.PAUSE = 0.3  ->  criar uma pausa para cada passo do código

# abrir o chrome
pyautogui.press("win")
pyautogui.write("chrome")
time.sleep(1)
pyautogui.click(x=567, y=733)
pyautogui.press("enter")
pyautogui.click(x=236, y=72)

# entrar no link
time.sleep(1)
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("enter")

# esperar o site carregar
time.sleep(1.9)

# 2- Fazer login
pyautogui.press("tab")
pyautogui.write("gusta1123@gmail.com")
pyautogui.press("tab") # passar para o campo de senha
pyautogui.write("12345678")
pyautogui.press("enter") #para clicar no login

time.sleep(1.5)

# 3- Importar a base de dados do produtos
import pandas

tabela = pandas.read_csv("produtos.csv")
# print(tabela)

pyautogui.press("tab")

for linha in tabela.index:

  # 4- Cadastrar o produto 
  time.sleep(1)
  
  #  .loc = localizar
  
  
  #preencher os camposMOLO000251  Logitech  Mouse 125.95  6.5 
  pyautogui.write(str(tabela.loc[linha, "codigo"]))
  pyautogui.press("tab")
  pyautogui.write(str(tabela.loc[linha, "marca"]))
  pyautogui.press("tab")
  pyautogui.write(str(tabela.loc[linha, "tipo"]))
  pyautogui.press("tab")
  pyautogui.write(str(tabela.loc[linha, "categoria"]))
  pyautogui.press("tab")
  pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
  pyautogui.press("tab")
  pyautogui.write(str(tabela.loc[linha, "custo"]))
  pyautogui.press("tab")
  pyautogui.write(str(tabela.loc[linha, "obs"]))

  obs = tabela.loc[linha, "obs"]
  if not pandas.isna(obs):
    pyautogui.write(str("sem obs"))
  
  
  # apertar para enviar
  # pyautogui.press("tab")
  pyautogui.press("enter")

  pyautogui.scroll(20000)
  pyautogui.click(x=949, y=250)
  time.sleep(0.5)


# enviar_email()

# 5- Repetior o processo para todos os produtos

