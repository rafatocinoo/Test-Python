# Solicitar al usuario una palabra
palabra = input("Introduce una palabra: ").lower()

# Definir las vocales
vocales = "aeiou"

# Crear un diccionario para contar las vocales
conteo_vocales = {vocal: 0 for vocal in vocales}

# Contar las veces que aparece cada vocal en la palabra
for letra in palabra:
    if letra in conteo_vocales:
        conteo_vocales[letra] += 1

# Mostrar los resultados
for vocal, conteo in conteo_vocales.items():
    print(f"La vocal '{vocal}' aparece {conteo} veces.")
