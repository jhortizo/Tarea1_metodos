"""modulo de soporte de la tarea 1, contiene funciones para:
 leer los archivos .pts , .tri
 hallar el área de triangulos a partir de los vértices

"""
import numpy as np

def leer_archivo(filename):
    archivo = []
    f = open(filename, 'r')
    for x in f:
#        print(x) #cada una de las filas del archivo pts
        x = x.replace('\t', ' ') #reemplaza cata tab por un espacio porque 
        #la lista es inhomogenea
        x = x.split(' ') #genera una lista cuyos elementos son las cosas 
        #que hayan entre dos espacios 
        coords = []
        for i in x:
            coords.append(float(i)) #volvemos los str de x en numeros
            #y los agregamos ala ultima casilla de coords
#        print(coords)
        archivo.append(coords) #hacemos la lista de listas
    archivo= np.array(archivo) #convertimos la lista de listas en array de np
    return archivo

def area_triangulo(A1,A2,A3):
    lado_1 = A1-A2
    lado_2 = A1-A3
    area = (1/2)*np.linalg.norm(np.cross(lado_1,lado_2))
    
    return area

def prom_altura(A1,A2,A3):
    hprom= (A1[2] + A2[2] + A3[2])/3
    return hprom

def area_triangulo_proyeccion(A1,A2,A3):

    A1[2]=0
    A2[2]=0
    A3[2]=0
    lado_1 = A1-A2
    lado_2 = A1-A3
    area = (1/2)*np.linalg.norm(np.cross(lado_1,lado_2))
    
    return area

#A1=np.array([5,0,0])
#A2=np.array([0,4,0])
#A3=np.array([0,0,1])
#print(area_triangulo_proyeccion(A1,A2,A3))
