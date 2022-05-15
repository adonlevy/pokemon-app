import requests
from multiprocessing import Pool


def get_pokemon(x):
    # Contact API
    try:
        url = f"https://pokeapi.co/api/v2/pokemon/{x+1}/"
        response = requests.get(url)
        response.raise_for_status()
    except requests.RequestException:
        return None

    # Parse response
    try:
        info = response.json()
        # get only the info I want to show on screen
        pokemon_info = {
            "pokedex": info["id"],
            "name": info["name"],
            "height": info["height"],
            "weight": info["weight"],
            "sprite": info["sprites"]["front_default"]
        }
    except (KeyError, TypeError, ValueError):
        return None
    # return the list of pokemon and the values I want
    return pokemon_info


def search_pokemon(name):
    try:
        url = f"https://pokeapi.co/api/v2/pokemon/{name.lower()}/"
        response = requests.get(url)
        response.raise_for_status()
    except requests.RequestException:
        return None

    # Parse response
    try:
        info = response.json()
        # get only the info I want to show on screen
        d = {
            "pokedex": info["id"],
            "name": info["name"],
            "height": info["height"],
            "weight": info["weight"],
            "sprite": info["sprites"]["front_default"]
        }
        return d
        # append the info to a new list that I will return
    except (KeyError, TypeError, ValueError):
        return None
