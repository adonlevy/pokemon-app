import requests
from multiprocessing import Pool

list_of_pokemon = []


def get_pokemon(i):
    # Contact API
    try:
        url = f"https://pokeapi.co/api/v2/pokemon/{i+1}/"
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

        # append the info to a new list that I will return

       # print(list_of_pokemon)

    except (KeyError, TypeError, ValueError):
        return None

# return the list of pokemon and the values I want
    return pokemon_info


if __name__ == '__main__':
    p = Pool()
    numbers = range(50)
    result = p.map(get_pokemon, numbers)

    p.close()
    p.join()
    print(result)
    for i in range(len(result)):
        print(result[i]["pokedex"])
