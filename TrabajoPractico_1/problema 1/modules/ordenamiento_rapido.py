from random import randint 


def ordenamientoRapido(unaLista):  #definimos la funcion
   ordenamientoRapidoAuxiliar(unaLista, 0, len(unaLista)-1) #Llama a una función auxiliar llamada ordenamientoRapidoAuxiliar. Le pasa la lista (unaLista), el índice del primer elemento (0), y el índice del último elemento (len(unaLista)-1). Esta función auxiliar es la que realmente implementa la lógica recursiva del Quicksort.
def ordenamientoRapidoAuxiliar(unaLista,primero,ultimo): #Define la función auxiliar ordenamientoRapidoAuxiliar que toma tres argumentos
   if primero<ultimo: #Esta es la condición base para la recursión. Si el índice del primer elemento (primero) es menor que el índice del último elemento (ultimo), significa que la sublista tiene al menos dos elementos y necesita ser ordenada. Si primero es igual o mayor que ultimo, la sublista tiene cero o un elemento, que ya está ordenado.

       puntoDivision = particion(unaLista,primero,ultimo) #Llama a la función particion para dividir la sublista actual en dos partes: los elementos menores que un "pivote" y los elementos mayores que el pivote. La función particion devuelve el índice del "punto de división" (la posición final del pivote después de la partición).

       ordenamientoRapidoAuxiliar(unaLista,primero,puntoDivision-1)#Realiza una llamada recursiva a ordenamientoRapidoAuxiliar para ordenar la sublista que está a la izquierda del puntoDivision (desde el primer elemento hasta el elemento justo antes del pivote).
       ordenamientoRapidoAuxiliar(unaLista,puntoDivision+1,ultimo) #Realiza una llamada recursiva a ordenamientoRapidoAuxiliar para ordenar la sublista que está a la izquierda del puntoDivision (desde el primer elemento hasta el elemento justo antes del pivote).
def particion(unaLista,primero,ultimo): #Define la función particion que toma la lista y los índices del primer y último elemento de la sublista a particionar.
   valorPivote = unaLista[primero] # Selecciona el primer elemento de la sublista como el "pivote". Los elementos de la sublista se compararán con este valor pivote.

   marcaIzq = primero+1
   marcaDer = ultimo

   hecho = False #Inicializa una variable booleana hecho a False. Esta variable se utilizará para controlar el bucle while principal de la partición.
   while not hecho: #Inicia un bucle while que continuará hasta que la variable hecho se establezca en True (lo que ocurre cuando las marcas izquierda y derecha se cruzan).

       while marcaIzq <= marcaDer and unaLista[marcaIzq] <= valorPivote:#Este bucle while interno mueve la marcaIzq hacia la derecha mientras no se cruce con marcaDer y el elemento en marcaIzq sea menor o igual que el valorPivote. El objetivo es encontrar un elemento en el lado izquierdo que sea mayor que el pivote.
           marcaIzq = marcaIzq + 1

       while unaLista[marcaDer] >= valorPivote and marcaDer >= marcaIzq: #Este bucle while interno mueve la marcaDer hacia la izquierda mientras no se cruce con marcaIzq y el elemento en marcaDer sea mayor o igual que el valorPivote. El objetivo es encontrar un elemento en el lado derecho que sea menor que el pivote.
           marcaDer = marcaDer -1

       if marcaDer < marcaIzq: #Si la marcaDer se ha movido a la izquierda de la marcaIzq, significa que se han encontrado todos los elementos mayores que el pivote a la izquierda y todos los elementos menores que el pivote a la derecha, por lo que la partición de esta sublista está completa.
           hecho = True # para salir del while
       else: #Si marcaDer aún no ha cruzado marcaIzq, significa que se han encontrado elementos en los lados incorrectos (un elemento mayor que el pivote a la izquierda y un elemento menor que el pivote a la derecha), y deben ser intercambiados.
           temp = unaLista[marcaIzq] #Guarda el valor del elemento en marcaIzq en una variable temporal temp.
           unaLista[marcaIzq] = unaLista[marcaDer] # naLista[marcaIzq] = unaLista[marcaDer]: Reemplaza el elemento en marcaIzq con el elemento en marcaDer
           unaLista[marcaDer] = temp # Reemplaza el elemento en marcaDer con el valor que se guardó en temp (el valor original del elemento en marcaIzq). Estas tres líneas realizan el intercambio de los elementos.

   temp = unaLista[primero] #Después de que el bucle while principal termina (cuando las marcas se cruzan), esta línea guarda el valor del pivote (que estaba al principio de la sublista) en la variable temp.
   unaLista[primero] = unaLista[marcaDer] #Coloca el elemento en marcaDer (que ahora es el elemento más grande de la partición izquierda o un elemento menor que el pivote) en la posición del pivote (al principio de la sublista).
   unaLista[marcaDer] = temp # Coloca el valor original del pivote en la posición de marcaDer. Ahora el pivote está en su posición final correcta dentro de la sublista particionada, con todos los elementos menores a su izquierda y todos los elementos mayores a su derecha.

   return marcaDer #Devuelve el índice de la posición final del pivote (marcaDer), que es el "punto de división".


if __name__ == "__main__":
    
    M, N = 500, 8000
    datos = [randint(0, M) for i in range(N)]
    
    print(datos)
    #datos_ordenados = sorted(datos)
    
    datos1 = ordenamientoRapido(datos)
    print("Lista ordenada :")
    
    print(datos)
    assert datos == datos_ordenados
#unaLista = [54,26,93,17,77,31,44,55,20]

#ordenamientoRapido(unaLista)

#print(unaLista)