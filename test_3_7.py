# test-ej-3.7.py
import unittest
from ej_3_7 import filtrar_abecedario  # Importamos la función desde el archivo original

class TestFiltrarAbecedario(unittest.TestCase):
    def test_abecedario_modificado(self):
        # Resultado esperado: letras en posiciones que no son múltiplos de 3
        resultado_esperado = ['a', 'b', 'd', 'e', 'g', 'h', 'j', 'k', 'm', 'n', 'p', 'q', 's', 't', 'v', 'w', 'y', 'z']
        
        # Llamamos a la función a probar
        resultado = filtrar_abecedario()
        
        # Verificamos que el resultado sea el esperado
        self.assertEqual(resultado, resultado_esperado)

if __name__ == "__main__":
    unittest.main()
