# ej_3_9.py

# Función que cuenta las vocales en una palabra
def contar_vocales(palabra):
    palabra = palabra.lower()
    vocales = "aeiou"
    conteo_vocales = {vocal: 0 for vocal in vocales}

    for letra in palabra:
        if letra in conteo_vocales:
            conteo_vocales[letra] += 1

    return conteo_vocales

# Solicitar al usuario una palabra
if __name__ == "__main__":
    palabra = input("Introduce una palabra: ").lower()

    # Llamar a la función para contar las vocales
    resultado = contar_vocales(palabra)

    # Mostrar los resultados
    for vocal, conteo in resultado.items():
        print(f"La vocal '{vocal}' aparece {conteo} veces.")
