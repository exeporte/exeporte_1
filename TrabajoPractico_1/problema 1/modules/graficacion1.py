# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 13:02:03 2022

@author: jinsfran

Medición de tiempos de ejecución y graficación
    Escriba un programa que permita medir el tiempo de ejecución de una función que obtiene todas las combinaciones de una lista de n números creados al azar tomando los números de a r valores. El programa debe medir el tiempo de ejecución para los valores de r en el rango de 1 a n.
    Para encontrar las combinaciones, puede utilizar la función “combinations” del módulo “itertools” o crear su propio algoritmo.
    El programa debe crear un gráfico que muestre el tiempo de ejecución versus r. El gráfico debe tener título, leyendas en ambos ejes, una grilla y un marcador que indique el máximo tiempo.
    Indicar, analizando la gráfica el valor de r para el cual el tiempo de ejecución es mayor.
"""

import random
import itertools
import time
import matplotlib.pyplot as plt

n = 21

# generar lista con números aleatorios
lista = [random.randint(-10, 10) for i in range(n)]

rs = [r+1 for r in range(n)]
tiempos = []

for r in rs:
    tic = time.perf_counter()
    combinaciones = list(itertools.combinations(lista, r))
    toc = time.perf_counter()
    delta_t = toc - tic
    tiempos.append(delta_t)

plt.plot(rs, tiempos)
plt.title('Tiempo versus cantidad de elementos en la combinación')
plt.xlabel('r')
plt.ylabel('tiempos ($s$)')
axes = plt.gca() # se obtienen los ejes actuales
axes.set_xticks([tick for tick in range(1, n+1)])

# Marcador
t_max = max(tiempos)
pos_r_max = tiempos.index(t_max) # no es la forma más eficiente
plt.scatter(rs[pos_r_max], 1.05*t_max, color='r', marker=7, s=100)

print(pos_r_max, rs[pos_r_max], round(t_max, 3))

# modificar fuente
# fuente = {'family': 'normal',  'weight': 'bold',  'size': 20}
fuente = {'family': 'normal',  'size': 12}
plt.rc('font', **fuente)  # runtime configuration (rc)
plt.grid()
plt.savefig('img/grafico_01.png')

# combinaciones = list(itertools.combinations([1, 2, 3, 4], 3))
# permutaciones = list(itertools.permutations([1, 2, 3, 4], 3))