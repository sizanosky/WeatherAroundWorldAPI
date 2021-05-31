"""
* Módulo 20 - Weather Around the world - Consumindo API
* Criado por Marcos Fabricio Sizanosky
* Professor: Jefferson Santos
* Data criação: 31/05/2021
  Programa em Python 3 para pesquisar o clima em qualquer cidade usando
   API OpenWeather.
"""
import requests
from helpers import *
from config import *

cabecalho()
print("\nAcesse dados meteorológicos atuais para qualquer local na Terra, \n"
      "incluindo mais de 200.000 cidades! meteorológicas. ")

nome_cidade = input("\nDigite o nome da cidade: ")

# api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}
url_completa = f"{URL_BASE}q={nome_cidade}&appid={API_KEY}"
print(url_completa)

dados_recebidos = requests.get(url_completa).json()
print(dados_recebidos)

if dados_recebidos['cod'] != '404':
      #  Dados chave main

      principal = dados_recebidos['main']
      temp_atual = principal['temp']
      pressao_atual = principal['pressure']
      humidade_atual = principal['humidity']

      # Dados chave "weather"
      clima = dados_recebidos['weather']
      descricao_clima = clima[0]['description']

else:
      print("Erro!!! Cidade não encontrada!")

