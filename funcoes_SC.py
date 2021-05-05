# -*- coding: utf-8 -*-
"""
Created on Mon May  3 12:41:04 2021

@author: Lais Nascimento
"""


from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver import ActionChains
import pandas as pd

def tentativa(numero_de_tentativas, css_code_selector,driver):
    
    #numero da tentativa atual
    tentativa_atual = 0 
    
    #define um número limite de tentativas
    while tentativa_atual <= numero_de_tentativas:
        
        #tenta clicar no botão
        try:
            driver.find_element_by_css_selector(css_code_selector).click()
            break
        
        #caso não funcione, aumenta a tentativa
        except:
            tentativa_atual += 1
    
    #caso o número de tentativas seja igual ao número limite, não foi possível concluir 
    #a ação
    if tentativa_atual == numero_de_tentativas:
        print("Número de tentativas excedidas")
        
    #caso contrário, informa que passou no teste
    else:
        print("Pass tentativa!")
    
    return


def acha_lista_de_links_consulta(numero_de_tentativas, css_code_selector, driver):
    i=2
    lista_links = []
    
    elementos = None
    
    
    tentativa_atual = 0 
    
    
    while tentativa_atual < numero_de_tentativas:
      
        try:
            
            while(i<13):
                elementos = driver.find_element_by_xpath('/html/body/div[2]/table/tbody/tr['+str(i)+']/td[3]/a')
                                                     

                #print(elementos)                                  
               
                link = elementos.get_attribute("href")
                #print(link)
                lista_links.append(link)
                

                
                i+=1
            break
        
        #caso não funcione, aumenta a tentativa
        except:
            tentativa_atual += 1
            
    #caso o número de tentativas seja igual ao número limite, não foi possível concluir 
    #a ação
    if tentativa_atual == numero_de_tentativas:
        print("Número de tentativas excedidas")
    
    #caso contrário, informa que passou no teste
    else:
        
        print("Pass acha_lista!")
        #print(elementos[0].text)
        
    return lista_links

def acha_lista_de_links_beneficarios(numero_de_tentativas, css_code_selector, driver):
    i=1
    lista_links = []
    
    elementos = None
    
    
    tentativa_atual = 0 
    
    
    while tentativa_atual < numero_de_tentativas:
      
        try:
            
            while(i<2170):
                elementos = driver.find_element_by_xpath('/html/body/div[2]/table/tbody/tr['+str(i)+']/td[1]/a')
                    
                                                                      

                #print(elementos)                                  
               
                link = elementos.get_attribute("href")
                #print(link)
                lista_links.append(link)
                

                
                i+=1
            break
        
        #caso não funcione, aumenta a tentativa
        except:
            tentativa_atual += 1
            
    #caso o número de tentativas seja igual ao número limite, não foi possível concluir 
    #a ação
    if tentativa_atual == numero_de_tentativas:
        print("Número de tentativas excedidas")
    
    #caso contrário, informa que passou no teste
    else:
        
        print("Pass acha_lista!")
        #print(elementos[0].text)
        
    return lista_links

def acha_lista_de_links_transferencia(numero_de_tentativas, css_code_selector, driver):
    i=1
    lista_links = []
    
    elementos = None
    
    
    tentativa_atual = 0 
    
    
    while tentativa_atual < numero_de_tentativas:
      
        try:
            
            while(i<20):
                elementos = driver.find_element_by_xpath('/html/body/div[2]/table/tbody/tr['+str(i)+']/td[3]/a')
                       

                #print(elementos)                                  
               
                link = elementos.get_attribute("href")
                #print(link)
                lista_links.append(link)
                

                
                i+=1
            break
        
        #caso não funcione, aumenta a tentativa
        except:
            tentativa_atual += 1
            
    #caso o número de tentativas seja igual ao número limite, não foi possível concluir 
    #a ação
    if tentativa_atual == numero_de_tentativas:
        print("Número de tentativas excedidas")
    
    #caso contrário, informa que passou no teste
    else:
        
        print("Pass acha_lista!")
        #print(elementos[0].text)
        
    return lista_links

def acha_lista_de_informacoes(numero_de_tentativas, css_code_selector, driver):
    i=1
    lista_infos = []
    
    elementos = None
    
    
    tentativa_atual = 0 
    
    
    while tentativa_atual < numero_de_tentativas:
      
        try:
            
            while(i<7):
                if i==1:
                    elementos = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/table/tbody/tr[3]/td')
                    #elementos = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/table/tbody/tr[3]/td')
                                                        
                    
                elif i==2:
                    elementos = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/table/tbody/tr[4]/td')
                    #elementos = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/table/tbody/tr[4]/td')
                
                elif i==3:
                    elementos = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/table/tbody/tr[5]/td')
                    #elementos = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/table/tbody/tr[5]/td')
                
                elif i==4:
                    elementos = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/table/tbody/tr[14]/td/a')
                    #elementos = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/table/tbody/tr[14]/td/a')
                
                elif i==5:
                    elementos = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/table/tbody/tr[17]/td')
                    #elementos = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/table/tbody/tr[17]/td')
                
                elif i==6:
                    elementos = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/table/tbody/tr[20]/td')
                    #elementos = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/table/tbody/tr[20]/td')
                    
               
                    

                lista_infos.append(elementos.text)

                
                i+=1
            break
        
        #caso não funcione, aumenta a tentativa
        except:
            tentativa_atual += 1
            
    #caso o número de tentativas seja igual ao número limite, não foi possível concluir 
    #a ação
    if tentativa_atual == numero_de_tentativas:
        print("Número de tentativas excedidas")
    
    #caso contrário, informa que passou no teste
    else:
        
        print("Pass acha_lista!")
        #print(elementos[0].text)
        
    return lista_infos

