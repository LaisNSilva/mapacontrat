# -*- coding: utf-8 -*-
"""
Created on Mon May  3 12:52:20 2021

@author: Lais Nascimento
"""


from tkinter import *

from tkinter.ttk import *
import re
from textblob import TextBlob
from tqdm.auto import tqdm
from tkinter import Label
import time

from funcoes_SC import *

import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver import ActionChains
from bs4 import BeautifulSoup



# n = 1
# links_consulta = []

# while n <= 1:
#     url = "http://sistemas2.sc.gov.br/sef/sctransf/Pesquisa/porInstrumento#"
    
#     driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')

   
#     driver.get(url)
  
#     time.sleep(60)
    
    
#     tentativa(1000, "#ngo > div.ngo-popup > div.got-it", driver)

#     lista_de_links_consulta = acha_lista_de_links_consulta(1000, "#ngo > div.celValor linkbefore 2017-linha > div", driver)


#     for elemento in lista_de_links_consulta:
#         links_consulta.append(elemento) #(elemento.text)
    
    

#     n+=1
#     driver.close()
    
# del(links_consulta[len(links_consulta)-1])
# print(links_consulta)

links_consulta = ['http://sistemas2.sc.gov.br/sef/sctransf/Pesquisa/porInstrumentoAno?palavraChave=2&ano=2014']

e = 0
beneficiarios=[]
while e <len(links_consulta): # 1 para testar depois colocar len(links_consulta)
    url = links_consulta[e]
    
    driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')

   
    driver.get(url)
  
    time.sleep(5)
    
    
    tentativa(1000, "#ngo > div.ngo-popup > div.got-it", driver)

    lista_de_links_beneficiarios = acha_lista_de_links_beneficarios(1000, "#ngo > div.celValor linkbefore 2017-linha > div", driver)


    for elemento in lista_de_links_beneficiarios:
        beneficiarios.append(elemento) #(elemento.text)
    
    

    e+=1
    driver.close()

print(beneficiarios)
print(len(beneficiarios))


i=0
transferencia=[]

while i <len(beneficiarios): # 1 para testar depois colocar len(links_consulta)
    url = beneficiarios[i]
    
    driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')

   
    driver.get(url)
  
    time.sleep(5)
    
    
    tentativa(1000, "#ngo > div.ngo-popup > div.got-it", driver)

    lista_de_links_transferencia = acha_lista_de_links_transferencia(1000, "#ngo > div.celValor linkbefore 2017-linha > div", driver)

    
    for elemento in lista_de_links_transferencia:
        transferencia.append(elemento) #(elemento.text)
    
    

    i+=1
    driver.close()

print(transferencia)


infos=0
informacoes=[]

while infos < len(transferencia): # 1 para testar depois colocar len(links_consulta)
    url = transferencia[infos]
    
    driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')

   
    driver.get(url)
  
    time.sleep(5)
    
    
    tentativa(1000, "#ngo > div.ngo-popup > div.got-it", driver)

    lista_de_informacoes = acha_lista_de_informacoes(1000, "#ngo > div.celValor linkbefore 2017-linha > div", driver)


    
    informacoes.append(lista_de_informacoes) #(elemento.text)
    
    
    #print(lista_de_informacoes)
    infos+=1
    driver.close()

print(informacoes)

dic_benef = []
dic_concedente=[]
dic_objeto=[]
dic_valorRep=[]
dic_dataAss=[]
dic_dataFim=[]

for listas in informacoes:
    dic_benef.append(listas[0])
    dic_concedente.append(listas[1])
    dic_objeto.append(listas[2])
    dic_valorRep.append(listas[3])
    dic_dataAss.append(listas[4])
    dic_dataFim.append(listas[5])
    
    
dicionario = {}
dicionario["Beneficiário"] = dic_benef
dicionario["Concedente"] = dic_concedente
dicionario["Objeto"] = dic_objeto
dicionario["Valor do Repasse"] = dic_valorRep
dicionario["Data de Assinatura"] = dic_dataAss
dicionario["Data de fim de Vigência"] = dic_dataFim


resultado = pd.DataFrame(data=dicionario)


resultado.to_excel('SC_Convenios_2014.xlsx', index = False)



