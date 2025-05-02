from random import randint
import time
import matplotlib.pyplot as plt

import ordenamiento_burbuja

def medir_tiempos(metodo_ord, tamanos):
    tiempos_ord_burb = []
    tiempos_ord_selecc = []
    tiempos_ord_selecc = []

    for n in tamanos:
        # datos = []
        # for _ in range(n):
        #     datos.append(randint(1, 10000))
        datos = [randint(1, 10000) for _ in range(n)]

        inicio = time.perf_counter()
        metodo_ord(datos)
        fin = time.perf_counter()
        tiempos_ord_burb.append(fin - inicio)
        
        print(f"Tiempo de ordenamiento burbuja para n={n}: {fin - inicio:.6f} segundos")
    
    return tiempos_ord_burb

if __name__ == '__main__':
    tamanos = [1, 10, 100, 200, 500, 700, 1000]
    medir_tiempos(ordenamiento_burbuja.ordenamiento_burbuja,tamanos)
    