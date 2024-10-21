# Función que cuenta las vocales en una palabra
def contar_vocales(palabra):
    palabra = palabra.lower()
    vocales = "aeiou"
    conteo_vocales = {vocal: 0 for vocal in vocales}

    for letra in palabra:
        if letra in conteo_vocales:
            conteo_vocales[letra] += 1

    return conteo_vocales

# Función para realizar pruebas
def test_contar_vocales():
    # Lista de casos de prueba
    casos_de_prueba = [
        ("murcielago", {'a': 2, 'e': 1, 'i': 1, 'o': 1, 'u': 1}),
        ("xyz", {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}),
        ("aeropuerto", {'a': 1, 'e': 1, 'i': 0, 'o': 1, 'u': 2}),
        ("AEIOU", {'a': 1, 'e': 1, 'i': 1, 'o': 1, 'u': 1}),
        ("banana", {'a': 3, 'e': 0, 'i': 0, 'o': 0, 'u': 0}),
    ]

    # Ejecutar pruebas
    for palabra, resultado_esperado in casos_de_prueba:
        resultado_obtenido = contar_vocales(palabra)
        assert resultado_obtenido == resultado_esperado, f"Error: para '{palabra}' se esperaba {resultado_esperado} y se obtuvo {resultado_obtenido}"

    print("Todas las pruebas pasaron.")

# Ejecutar las pruebas
test_contar_vocales()
