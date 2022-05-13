import requests


def main():
    print(api())


def api():
    # Contact API
    try:
        url = "https://pokeapi.co/api/v2/pokemon/ditto"
        response = requests.get(url)
        response.raise_for_status()
    except requests.RequestException:
        return None

    # Parse response
    try:
        info = response.json()
        return {
            "pokedex": info["id"],
            "name": info["name"],
            "moves": info["moves"][0]["move"]["name"]
        }
    except (KeyError, TypeError, ValueError):
        return None


main()
