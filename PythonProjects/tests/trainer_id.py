import requests
import pytest

TOKEN = 'c79c4403f7d99c380287f68629b4d85a'
URL = 'https://api.pokemonbattle.ru/v2/trainers'
HEADERS = {
    'Content-Type': 'application/json',
    'trainer_token': TOKEN
}
TRAINER_ID = 12765

def test_response_contains_trainer_name():
    url = f"{URL}/{TRAINER_ID}"
    response = requests.get(url, headers=HEADERS)
    assert response.status_code == 200
    response_data = response.json()
    assert "name" in response_data
    assert response_data["name"] == "Повар"  