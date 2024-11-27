import requests
from config import token_bs

auth = {'Authorization': f'Bearer {token_bs}'}

url = 'https://api.brawlstars.com/v1/players/%23prgg89jl'

response = requests.get(url, headers=auth).json()


def trophies():
    return response.get('trophies')


def victories():
    return response.get('soloVictories'), response.get('duoVictories'), response.get('3vs3Victories')


def sum_victories():
    return response.get('soloVictories') + response.get('duoVictories') + response.get('3vs3Victories')


def nickname():
    return response.get('name')

