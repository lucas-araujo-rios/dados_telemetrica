from pandas import pd
import requests

response = requests.get("https://dadosabertos.aneel.gov.br/dataset/5e0fafd2-21b9-4d5b-b622-40438d40aba2/resource/c189442a-18f0-44eb-9c89-3b48147a4d65/download/empreendimento-gd-informacoes-tecnicas-hidreletrica.csv")

print(response.content)