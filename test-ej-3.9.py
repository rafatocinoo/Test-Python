# test-ej-3.9.py
import unittest
from eje_3_9 import contar_vocales  # Importamos la función desde el archivo original

class TestContarVocales(unittest.TestCase):
    def test_casos_varios(self):
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
            with self.subTest(palabra=palabra):
                resultado_obtenido = contar_vocales(palabra)
                self.assertEqual(resultado_obtenido, resultado_esperado)

if __name__ == "__main__":
    unittest.main()
