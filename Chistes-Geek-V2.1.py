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

def traducir_chiste(chiste, idioma="es"):
    """
    Traduce el chiste a un idioma específico usando Google Translate.
    """
    try:
        traductor = GoogleTranslator(source='auto', target=idioma)
        chiste_traducido = traductor.translate(chiste)
        return chiste_traducido
    except Exception as e:
        # Manejo de errores de traducción
        print(f"Error al traducir chiste: {e}")
        return chiste  # Devuelve el chiste original si falla la traducción

def guardar_chiste(chiste):
    """
    Guarda un chiste en un archivo de texto.
    """
    with open("chistes_favoritos.txt", "a") as archivo:
        archivo.write(chiste + "\n")

def ver_chistes_favoritos():
    """
    Muestra los chistes guardados en un archivo de texto.
    """
    try:
        with open("chistes_favoritos.txt", "r") as archivo:
            chistes = archivo.readlines()
            if chistes:
                for chiste in chistes:
                    print(chiste.strip())
            else:
                print("No hay chistes guardados.")
    except FileNotFoundError:
        print("No hay chistes guardados.")

def mostrar_menu():
    """
    Muestra el menú de opciones al usuario.
    """
    print("\nMenú:")
    print("1. Obtener un nuevo chiste")
    print("2. Ver chistes favoritos")
    print("3. Salir")
    return input("Selecciona una opción: ")

if __name__ == "__main__":
    while True:
        opcion = mostrar_menu()
        if opcion == "1":
            chiste_ingles = obtener_chiste_geek()
            if chiste_ingles:
                idioma = input("¿En qué idioma quieres el chiste? (es, en, fr, etc.): ")
                chiste_espanol = traducir_chiste(chiste_ingles, idioma)
                print(chiste_espanol)
                guardar = input("¿Quieres guardar este chiste? (s/n): ")
                if guardar.lower() == "s":
                    guardar_chiste(chiste_espanol)
            else:
                print("No se pudo obtener un chiste.")
        elif opcion == "2":
            ver_chistes_favoritos()
        elif opcion == "3":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida, intenta de nuevo.")