import requests

API_URL = "https://www.freetogame.com/api"

def obtener_juegos_mas_populares(limite=50):
    """
    Obtiene los juegos más populares de todos los géneros y plataformas.
    """
    params = {
        "sort-by": "popularity"
    }

    response = requests.get(f"{API_URL}/games", params=params)

    if response.ok:
        juegos = response.json()
        return juegos[:limite]
    else:
        print(" Error al conectarse a la API:", response.status_code)
        return []
