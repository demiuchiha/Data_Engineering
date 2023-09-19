import requests
import json
from pprint import pprint

# Define tus credenciales de la API de Marvel
ts = 1
private_key = "2ddcd75350aaffcbb872933b8d8b59270b359aba"
public_key = "76d106de43253f7f4989755d6967375b"
hashed = "7c7fbb5b1d930d7e9c35069530f86ae9"

# URL base de la API de Marvel
base_url = f"https://gateway.marvel.com:443/v1/public/characters?ts={ts}&apikey={public_key}&hash={hashed}"

#print (base_url)

lista = []
response = requests.get(base_url)
if response.status_code == 200:
    response_json = json.loads(response.text)

    for i in response_json["data"]["results"]:
        nombre = i["name"]
        descripcion = i["description"]
        comics_disponibles = i["comics"]["available"]
        series_disponibles = i["series"]["available"]
        dic = {"nombre": nombre, "descripcion": descripcion, "comics_disponibles": comics_disponibles, "series_disponibles": series_disponibles}
        lista.append(dic)
print(lista)
