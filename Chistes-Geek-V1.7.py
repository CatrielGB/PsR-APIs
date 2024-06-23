import requests
from deep_translator import GoogleTranslator

def obtener_chiste_geek():
    """
    Obtiene un chiste geek en inglés desde la API de Geek Jokes.
    """
    url = "https://geek-jokes.sameerkumar.website/api?format=json"
    try:
        respuesta = requests.get(url)
        respuesta.raise_for_status()  # Verifica si hay errores HTTP
        datos = respuesta.json()
        return datos.get('joke', "No se encontró ningún chiste.")
    except requests.exceptions.RequestException as e:
        # Manejo de errores de solicitud HTTP
        print(f"Error al obtener chiste: {e}")
        return None

def traducir_chiste(chiste):
    """
    Traduce el chiste del inglés al español usando Google Translate.
    """
    try:
        traductor = GoogleTranslator(source='auto', target='es')
        chiste_traducido = traductor.translate(chiste)
        return chiste_traducido
    except Exception as e:
        # Manejo de errores de traducción
        print(f"Error al traducir chiste: {e}")
        return chiste  # Devuelve el chiste original si falla la traducción

if __name__ == "__main__":
    print("Aquí tienes un chiste geek:")
    chiste_ingles = obtener_chiste_geek()
    if chiste_ingles:
        chiste_espanol = traducir_chiste(chiste_ingles)
        print(chiste_espanol)
    else:
        print("No se pudo obtener un chiste.")
