#Проверка кода ответа на запрос GET /trainers

import requests
import pytest

TOKEN = 'c79c4403f7d99c380287f68629b4d85a'
URL = 'https://api.pokemonbattle.ru/v2/trainers'
HEADERS = {
    'Content-Type': 'application/json',
    'trainer_token': TOKEN 
    }

def test_get_trainers():
    response = requests.get(URL, headers=HEADERS)
    try:
        assert response.status_code == 200
        print("Тест пройден: ответ пришел с кодом 200")
    except AssertionError:
        print(f"Тест не пройден: ожидался код 200, пришел код {response.status_code}")

import json

TRAINER_ID = 12765
TOKEN = 'c79c4403f7d99c380287f68629b4d85a'
URL = 'https://api.pokemonbattle.ru/v2/trainers'
HEADERS = {
    'Content-Type': 'application/json',
    'trainer_token': TOKEN
}

def test_response_contains_trainer_name():
    url = f'{URL}/?trainer_id={TRAINER_ID}'
    response_get = requests.get(url, headers=HEADERS)
    assert response_get.status_code == 200
    response_data = response_get.json()
    assert response_data["data"][0]["trainer_name"] == "Повар"
    print("Это Повар")
    