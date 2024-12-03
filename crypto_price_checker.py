# Todos sabemos el interés que genera el precio de Bitcoin y sus oscilaciones.
# Hoy, vamos a desarrollar una API que extraiga el precio de la moneda en tiempo real.

import requests 

# Función para obtener el precio de las criptomonedas
def obtener_precio(ids, monedas):
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {"ids": ids, "vs_currencies": monedas}

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # Lanza una excepción si hay un error HTTP
        data = response.json()
        if not data:
            raise ValueError("No se obtuvo respuesta válida de la API.")
        return data
    except requests.exceptions.HTTPError as errh:
        print(f"Error HTTP: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Error de conexión: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Error de tiempo de espera: {errt}")
    except requests.exceptions.RequestException as err:
        print(f"Error en la solicitud: {err}")
    except ValueError as ve:
        print(f"Error: {ve}")
    return None

# Función para mostrar el precio de la criptomoneda
def mostrar_precio(cripto, price_usd, price_eur):
    print(f"El precio actual de {cripto.capitalize()} es:")
    print(f"  - ${price_usd:.2f} USD" if price_usd != "N/A" else "  - Precio en USD no disponible")
    print(f"  - €{price_eur:.2f} EUR" if price_eur != "N/A" else "  - Precio en EUR no disponible")

# Función principal
def main():
    # Solicitar entrada del usuario
    criptomonedas_input = input("Introduce las criptomonedas separadas por comas (ej. bitcoin, ethereum, binance): ")
    monedas_input = input("Introduce las monedas separadas por comas (ej. usd, eur): ")
    
    if not criptomonedas_input or not monedas_input:
        print("Error: Debes introducir al menos una criptomoneda y una moneda.")
        return

    # Limpiar y convertir las entradas
    criptomonedas = [cripto.strip().lower() for cripto in criptomonedas_input.split(',')]
    monedas = monedas_input.strip().lower()

    for cripto in criptomonedas:
        # Obtener el precio para cada criptomoneda
        datos = obtener_precio(cripto, monedas)
        if datos and cripto in datos:
            price_usd = datos[cripto].get("usd", "N/A")
            price_eur = datos[cripto].get("eur", "N/A")
            mostrar_precio(cripto, price_usd, price_eur)
        else:
            print(f"No se pudo obtener el precio de {cripto}. Puede que esté mal escrito o no exista.")

# Llamar a la función principal cuando se ejecute el script
if __name__ == "__main__":
    main()