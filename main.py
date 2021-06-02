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

while True:
    cabecalho()
    print("\nAcesse dados meteorológicos atuais para qualquer local na Terra, \n"
          "incluindo mais de 200.000 cidades! Processando dados meteorológicos \n"
          "de diferentes fontes, como modelos meteorológicos globais e locais, \n"
          "satélites, radares e uma vasta rede de estações meteorológicas. ")

    nome_cidade = input("\nDigite o nome da cidade: ")

    # api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}
    url_completa = f"{URL_BASE}q={nome_cidade}&appid={API_KEY}"
    #  print(url_completa)

    dados_recebidos = requests.get(url_completa).json()
    #  print(dados_recebidos)

    if dados_recebidos['cod'] != '404':
        principal = dados_recebidos['main']
        temp_atual = principal['temp']
        pressao_atual = principal['pressure']
        humidade_atual = principal['humidity']
        visibilidade_atual = dados_recebidos['visibility']

        # Dados chave "weather"
        clima = dados_recebidos['weather']
        descricao_clima = clima[0]['description']

        #  Mostrar os seguintes valores
        print(f"\n# Cidade..................: {nome_cidade.title()}")
        print(f"# Temperatura.............: {round(kelvin_para_celsius(temp_atual), 1)} Cº")
        print(f"# Umidade do ar...........: {humidade_atual}%")
        print(f"# Pressão atmosférica.....: {pressao_atual} hPa")
        print(f"# Visibilidade agora......: {visibilidade_atual / 1000} Km")
        print(f"# Descrição clima.........: {descricao_clima}")

    else:
        print("Erro >>> Cidade não encontrada!")

    valida_saida()
