import requests

TOKEN = 'c79c4403f7d99c380287f68629b4d85a'
URL = 'https://pokemonbattle.ru/v2/pokemons'
HEADERS = {
    'Content-Type': 'application/json',
    'Authorization': f'Token {TOKEN}'
}

pokemon_id = 171008
body = {
    "name": "Пирожок"
}
try:
    response = requests.put(f'{URL}/{pokemon_id}', headers=HEADERS, json=body)
    
    if response.status_code == 200:
        print("Успешная смена имени!")
    else:
        print(f"Произошла ошибка: {response.status_code}, {response.text}")
except Exception as e:
    print(f"Произошла ошибка при выполнении запроса: {e}")
