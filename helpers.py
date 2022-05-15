import requests


def get_pokemon(num, generation):
    # Contact API
    list_of_pokemon = []
    if generation == 1:
        starting_index = 1
    else:
        starting_index = 152

    for x in range(starting_index, num):
        try:
            url = f"https://pokeapi.co/api/v2/pokemon/{x}/"
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
            list_of_pokemon.append(pokemon_info)
        except (KeyError, TypeError, ValueError):
            return None
    # return the list of pokemon and the values I want
    return list_of_pokemon
