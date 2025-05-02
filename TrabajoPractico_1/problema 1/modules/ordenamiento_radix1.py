from random import randint 

def obtener_digito(numero, posicion_digito, base = 10):
    """
    Obtiene el dígito en la posición especificada (de derecha a izquierda) de un número.
    Devuelve cero si la posición es mayor que el número de dígitos del número.
    """
    return (numero // (base ** posicion_digito)) % base
def ordenamiento_radix(lista):
    """
    Ordena una lista de números enteros utilizando el algoritmo de ordenamiento Radix.
    """
    # Encuentra el número máximo para determinar el número de dígitos
    max_num = max(lista)
    exp = 1  # Exponente para la posición del dígito
    lista_aux = [[] for _ in range(10)]  
    pos = 0  # Inicializa la posición del dígito
    while max_num // exp > 0:
        # Coloca los números en la lista auxiliar según el dígito actual
        for num in lista:
            digit = obtener_digito(num, pos)  # Obtiene el dígito en la posición actual
            lista_aux[digit].append(num)

        # Reconstruye la lista original a partir de la lista auxiliar
        sig_pos = 0  # Inicializa la posición en la lista original
        for sublist in lista_aux:
            for num in sublist:
                lista[sig_pos] = num  # Añade el número a la lista original 
                sig_pos += 1    


        # Limpia la lista auxiliar para la siguiente posición de dígito
        lista_aux = [[] for _ in range(10)]

        # Aumenta el exponente para pasar al siguiente dígito
        exp *= 10
        pos += 1
 
 
    return lista


if __name__ == "__main__":
    
    M, N = 500, 8000
    datos = [randint(0, M) for i in range(N)]
    
    print(datos)
    datos_ordenados = sorted(datos)
    
    datos1 = ordenamiento_radix(datos)
    print("Lista ordenada :")
    
    print(datos1)
    assert datos == datos_ordenados
    
   

#ordenamiento_radix(datos1) #Esta línea llama a la función ordenamientoBurbuja y le pasa la lista unaLista como argumento. Después de que la función se ejecute, la lista unaLista habrá sido modificada para estar ordenada.
#print(datos)
#print(unaLista) # Esta línea imprime el contenido de la lista unaLista después de que la función ordenamientoBurbuja la haya ordenado. La salida será la lista original, pero ahora en orden ascendente.
#print(datos_ordenados)