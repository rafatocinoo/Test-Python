def filtrar_abecedario():
    # Almacenar el abecedario en una lista
    abecedario = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
    # Crear una nueva lista sin las letras en posiciones múltiplos de 3
    abecedario_modificado = []
    
    for i in range(len(abecedario)):
        if (i + 1) % 3 != 0:  # Verificamos si la posición (i + 1) no es múltiplo de 3
            abecedario_modificado.append(abecedario[i])
    
    return abecedario_modificado  # Retornamos la lista resultante
