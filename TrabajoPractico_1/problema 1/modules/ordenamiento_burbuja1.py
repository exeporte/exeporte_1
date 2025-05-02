
from random import randint
# -*- coding: utf-8 -*-
def ordenamiento_burbuja(unaLista):
    n = len(unaLista)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if unaLista[j] > unaLista[j + 1]:
                temp = unaLista[j]
                unaLista[j] = unaLista[j + 1]
                unaLista[j + 1] = temp
    return unaLista # Es importante retornar la lista ordenada
#def ordenamientoBurbuja(unaLista): #definicion de funcion ordenamiento Burbuja que toma un argumento: unaLista
 #   for extremo in range(len(unaLista)-1,0,-1): # bucle exterior Calcula el índice del último elemento de la lista y le resta 1. Esto se debe a que en cada pasada del bucle exterior, el elemento más grande "burbujea" hacia su posición correcta al final de la porción no ordenada de la lista. Por lo tanto, no necesitamos comparar los elementos que ya están en su lugar.
  #      for i in range(extremo): #Este es el bucle interior
   #         if unaLista[i]>unaLista[i+1]: #Esta línea realiza la comparación clave del algoritmo Burbuja
    #            temp = unaLista[i] #Si la condición del if es verdadera, esta línea guarda el valor del elemento actual (unaLista[i]) en una variable temporal llamada temp. Esto es necesario para poder intercambiar los valores sin perder uno de ellos.
     #           unaLista[i] = unaLista[i+1]#Esta línea reemplaza el valor del elemento actual (unaLista[i]) con el valor del elemento siguiente (unaLista[i+1]).
      #          unaLista[i+1] = temp# Esta línea reemplaza el valor del elemento siguiente (unaLista[i+1]) con el valor que se guardó previamente en la variable temporal temp (que era el valor original del elemento actual). Estas tres últimas líneas (temp = ..., unaLista[i] = ..., unaLista[i+1] = ...) realizan el intercambio de los dos elementos adyacentes.

if __name__ == '__main__':
    # ordena numeros y palabras
    M, N = 500, 8000
    datos = [randint(-M, M) for i in range(N)]
    
    
    datos_ordenados = sorted(datos)
    
    datos = ordenamiento_burbuja(datos)
    
    assert datos == datos_ordenados


#unaLista = [54,26,93,17,77,31,44,55,20]

ordenamiento_burbuja(datos) #Esta línea llama a la función ordenamientoBurbuja y le pasa la lista unaLista como argumento. Después de que la función se ejecute, la lista unaLista habrá sido modificada para estar ordenada.

#print(unaLista) # Esta línea imprime el contenido de la lista unaLista después de que la función ordenamientoBurbuja la haya ordenado. La salida será la lista original, pero ahora en orden ascendente.
print(datos_ordenados)

