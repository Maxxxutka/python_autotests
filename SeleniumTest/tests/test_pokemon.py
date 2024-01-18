import requests 
import pytest


def test_get_trainers_status_code():
    URL = 'https://api.pokemonbattle.me:9104'
    HEADER = {'Content-Type': 'application/json'}
    response = requests.get(url=f'{URL}/trainers', headers=HEADER, timeout=5)
    assert response.status_code == 200, 'Unexpected status code'

def test_my_name_in_body_response():
    URL = 'https://api.pokemonbattle.me:9104'
    HEADER = {'Content-Type': 'application/json'}
    response = requests.get(url=f'{URL}/trainers', headers=HEADER, params={'trainer_id': 4655})
    assert response.json()['trainer_name'] == 'Pupsen', 'Undefined name'

