"""
Primera tarea de metodos numericos 2019-1
Hecha por Sofía Obando, José Hernán Ortiz, Jose Manuel Rendón
Status:
    *Falta revisar los valores entregados para área y volumen
    *Falta buscar forma de graficar mejor el valle
    *Faltan hacer ejemplos y testeos de las funciones, y organizar los docstrings
"""


import tarea_1_funciones as fcn
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D



puntos = fcn.leer_archivo('valle_aburra.pts')
#print(puntos.shape) #se puede hacer porque es una array de np

elementos= fcn.leer_archivo('valle_aburra.tri')
# print(elementos.shape)
elementos = elementos.astype(int)
#
# elemento = elementos[1]
# print(elemento)
# print(puntos[elemento[0]], puntos[elemento[1]], puntos[elemento[2]])


area_total = 0
for elemento in elementos:
    area_elemento = fcn.area_triangulo(puntos[elemento[0]], puntos[elemento[1]], puntos[elemento[2]])
    area_total = area_total + area_elemento

print('El área del valle de Aburrá es: ', area_total)




volumen_total=0
hmin = np.amin(puntos[:, 2])
for elemento in elementos:
    area_elemento_proyeccion = fcn.area_triangulo_proyeccion(puntos[elemento[0]], puntos[elemento[1]], puntos[elemento[2]])
    volumen_elemento = area_elemento * ((fcn.prom_altura(puntos[elemento[0]], puntos[elemento[1]], puntos[elemento[2]]))-hmin)
    volumen_total=volumen_total+volumen_elemento
print('El volumen del valle de Aburrá, desde su punto más bajo, es: ', volumen_total)



fig = plt.figure()
ax = plt.axes(projection = '3d')
ax.plot(puntos[:, 0], puntos[:, 1], puntos[:, 2], 'ok')


plt.show()
