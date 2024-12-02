# Todos sabemos el interés que genera el precio de Bitcoin y sus oscilaciones.
# Hoy, vamos a desarrollar una API que extraiga el precio de la moneda en tiempo real.

import requests  # Importante para hacer solicitudes HTTP

# URL del endpoint de la API de CoinGecko
url = "https://api.coingecko.com/api/v3/simple/price"

# Información que queremos extraer de la web
params = {
    "ids": "bitcoin",  # Criptomoneda
    "vs_currencies": "usd,eur",  # Monedas destino: USD y EUR
}

try:
    # Hacemos la solicitud de la API
    response = requests.get(url, params=params)
    response.raise_for_status()  # Lanza una excepción si hay un error HTTP

    # Convertimos la respuesta de JSON a un diccionario de Python
    data = response.json()
    price_usd = data["bitcoin"]["usd"]  # Extraemos el precio en USD
    price_eur = data["bitcoin"]["eur"]  # Extraemos el precio en EUR

    # Imprimimos los precios con dos decimales
    print(f"El precio actual de Bitcoin es: ${price_usd:.2f} USD")
    print(f"El precio actual de Bitcoin es: €{price_eur:.2f} EUR")

except requests.exceptions.RequestException as e:  # Manejo de excepciones
    print(f"Error al obtener el precio: {e}")
