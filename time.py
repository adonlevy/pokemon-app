import time
from multiprocessing import Pool
import requests


def get_pokemon_serially(numbers):
    start = time.time()
    result = []
    for i in numbers:
        result.append(get_pokemon(i))
    end = time.time() - start
    print(f"Serial processing took {end} seconds")


def get_pokemon_with_mp(numbers):
    start = time.time()
    p = Pool()
    result = p.map(get_pokemon, numbers)
    p.close()
    p.join()
    end = time.time() - start
    print(f"Multiprocessing took {end} seconds")


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
    return pokemon_info


if __name__ == '__main__':
    numbers = range(150)

    get_pokemon_serially(numbers)
    get_pokemon_with_mp(numbers)
