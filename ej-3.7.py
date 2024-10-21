# Paso 1: Almacenar el abecedario en una lista
abecedario = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Paso 2: Crear una nueva lista sin las letras en posiciones múltiplos de 3
abecedario_modificado = []

for i in range(len(abecedario)):
    # Verificamos si la posición (i + 1) no es múltiplo de 3
    if (i + 1) % 3 != 0:
        abecedario_modificado.append(abecedario[i])

# Paso 3: Mostrar la lista resultante
print("Lista del abecedario sin letras en posiciones múltiplos de 3:")
print(abecedario_modificado)
