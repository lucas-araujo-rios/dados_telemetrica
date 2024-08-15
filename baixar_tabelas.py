from pandas import pd
import requests

def baixar_arquivo(url,pasta_destino):
    resposta = requests.get(url)
    with open()

nome_arquivos = [
    'empreendimento-geraca-distribuida.csv',
    'empreendimento-gd-informacoes-tecnicas-eolica.csv',
    'empreendimento-gd-informacoes-tecnicas-fotovoltaica.csv',
    'empreendimento-gd-informacoes-tecnicas-hidreletrica.csv',
    'empreendimento-gd-informacoes-tecnicas-telemetrica.csv'
    ]

for arquivo in nome_arquivos:
    baixar_arquivo(
        f'https://dadosabertos.aneel.gov.br/dataset/5e0fafd2-21b9-4d5b-b622-40438d40aba2/resource/b1bd71e7-d0ad-4214-9053-cbd58e9564a7/download/{arquivo}',
        pasta_destino)