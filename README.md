## Bitcoin & Cryptocurrency Price Checker ##
Este proyecto es un script en Python que permite consultar los precios de Bitcoin y otras criptomonedas en tiempo real utilizando la API pública de CoinGecko. Con esta herramienta, puedes consultar el precio de varias criptomonedas a la vez en monedas fiat como USD o EUR, obteniendo resultados precisos y formateados.

🚀 Características
Consulta múltiple: Introduce varias criptomonedas y monedas fiat para obtener precios en un solo paso.
Formato claro: Los precios se muestran con dos decimales para facilitar la lectura.
Manejo de errores robusto: El programa gestiona problemas de conexión, datos incompletos y entradas incorrectas.
Interfaz interactiva: Introduce datos fácilmente a través de la terminal.

🛠️ Requisitos
Python 3.x
Librería requests

📦 Instalación
Introduce las criptomonedas separadas por comas (ej. bitcoin, ethereum, binance): bitcoin, ethereum
Introduce las monedas separadas por comas (ej. usd, eur): usd, eur

El precio actual de Bitcoin es:
  - $57000.00 USD
  - €48000.00 EUR
El precio actual de Ethereum es:
  - $4000.00 USD
  - €3400.00 EUR
Si introduces una criptomoneda o moneda incorrecta, se mostrará un mensaje de error como:

bash
Copiar código
No se pudo obtener el precio de xyzcoin. Puede que esté mal escrito o no exista.
🧑‍💻 Estructura del Código
Funciones principales:
obtener_precio(ids, monedas):

Realiza la solicitud HTTP a la API de CoinGecko para obtener los precios.
Maneja errores comunes, como problemas de conexión o respuestas incompletas.
mostrar_precio(cripto, price_usd, price_eur):

Imprime los precios de las criptomonedas en formato claro.
main():

Solicita al usuario las criptomonedas y monedas a consultar.
Itera sobre las criptomonedas para obtener sus precios y mostrarlos.
Manejo de errores:
Errores de conexión y tiempo de espera.
Verificación de criptomonedas o monedas inexistentes.
Validación de entradas vacías.

⚠️ Errores Comunes
Sin conexión a Internet: Asegúrate de estar conectado a Internet, ya que el script depende de la API de CoinGecko.
Nombres incorrectos: Introduce correctamente los nombres de las criptomonedas y monedas. Consulta CoinGecko para obtener una lista válida.

📜 Licencia
Este proyecto está bajo la Licencia MIT. Puedes usar, modificar y distribuir este script libremente.

🤝 Contribuciones
¡Contribuciones son bienvenidas! Si tienes ideas o mejoras, no dudes en abrir un issue o enviar un pull request.

