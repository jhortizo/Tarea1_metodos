"""modulo de soporte de la tarea 1, contiene funciones para:
 leer los archivos .pts , .tri
 hallar el área de triangulos a partir de los vértices



"""
import numpy as np

def leer_archivo(filename):
    archivo = []
    f = open(filename, 'r')
    for x in f:
        x = x.replace('\t', ' ')
        x = x.split(' ')
        coords = []
        for i in x:
            coords.append(float(i))
#        print(coords)
        archivo.append(coords)
    archivo= np.array(archivo)
    return archivo

def area_triangulo(A1,A2,A3):
    lado_1 = A1-A2
    lado_2 = A1-A3
    area = (1/2)*np.linalg.norm(np.cross(lado_1,lado_2))
    return area

def prom_altura(A1,A2,A3):
    hprom= (A1[2] + A2[2] + A3[2])/3
    return hprom
