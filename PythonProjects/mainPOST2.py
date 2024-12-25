import requests

TOKEN = 'c79c4403f7d99c380287f68629b4d85a'
URL = 'https://pokemonbattle.ru/v2/trainers/add_pokeball'
HEADERS = {
    'Content-Type': 'application/json',
    'Authorization': f'Token {TOKEN}'
}

pokemon_id = 171008
body = {
    "pokemon_id": pokemon_id
}

try:
    response = requests.post(URL, headers=HEADERS, json=body)
    
    if response.status_code == 200:
        print("Покемон пойман!")
    else:
        print(f"Произошла ошибка: {response.status_code}, {response.text}")
except Exception as e:
    print(f"Произошла ошибка при выполнении запроса: {e}")