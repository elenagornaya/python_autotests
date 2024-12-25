import requests
import json

TOKEN = 'c79c4403f7d99c380287f68629b4d85a'
URL = 'https://api.pokemonbattle.ru/v2/pokemons'
HEADERS = {
    'Content-Type': 'application/json',
    'trainer_token': TOKEN 
}
body = {
    "name": "Хлебушек",
    "photo_id": 1
}

response = requests.post(URL, headers=HEADERS, json=body)
print(response.text)
