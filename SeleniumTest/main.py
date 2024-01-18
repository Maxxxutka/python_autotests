import requests

URL = 'https://api.pokemonbattle.me:9104'
HEADER = {'trainer_token': 'c44ddc730b9ab1b792de192ac9316e48', 'Content-Type': 'application/json'}
BODY = {
    "name": "Maxutkin",
    "photo": "https://dolnikov.ru/pokemons/albums/021.png"
}
response = requests.post(url=f'{URL}/pokemons', headers=HEADER, json=BODY, timeout=5)

print(response.text)

'''
'''
URL = 'https://api.pokemonbattle.me:9104'
HEADER = {'trainer_token': 'c44ddc730b9ab1b792de192ac9316e48', 'Content-Type': 'application/json'}
BODY = {
    "pokemon_id": 27948,
    "name": "Maxxxutki",
}
response = requests.put(url=f'{URL}/pokemons', json=BODY, headers=HEADER)

print(response.text)

'''
'''
URL = 'https://api.pokemonbattle.me:9104'
HEADER = {'trainer_token': 'c44ddc730b9ab1b792de192ac9316e48', 'Content-Type': 'application/json'}
BODY = {
    "pokemon_id": 27948
}

response = requests.post(url=f'{URL}/trainers/add_pokeball', headers=HEADER, json=BODY)

print(response.text)