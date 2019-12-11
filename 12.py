# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 14:23:47 2019

@author: stitch
"""

#ejersicio 12: 

#La superficie de la tierra es curva y la distancia entre grados de longitud varia con lla latitud
#como resultado, encontrar la distancia entre dos puntos de la superficie de la tierra 
#es mas complicado que usar el teorema de pitagoras.
#Si (t1, g1) y (t2,g2) es la latitud y longitud de dos puntos de la superficie de la tierra.
#La didtancia entre esos puntos, a traves de la superficie de la tierra, en kilometros es:
#distancia= 6371.01*arccos(sent(t1)*sen(t2)+cos(t1)*cos(t2)*cos(g1-g2))
#cree un programa que le permita al usuario introducir la latitud y longitud de dos puntos de la tierra en grados. Su programa debe desplegar la distancia entre
#esos puntos, en kilometros. Tenga en cuenta que las fucniones trigonometricas eh python
#trabajan en radianes, por lo que debe de convertir el valor introducido por el usuario
#en grados a radianes antes de utilizar la formula. El modulo

import math 

lat=int(input("ingresa latitud t1: "))
lati=int(input("ingresa latitud g1: "))
lon=int(input("ingresa longitud t2: "))
long=int(input("ingresa longitud g2: "))
lat1=(math.pi*(lat))/180    #t1
lon1=(math.pi*(lon))/180    #t2
lat2=(math.pi*(lati))/180    #g1

lon2=(math.pi*(long))/180    #g2
print('latitud t1 en radianes: '+str(lat1))
print('longitud g1 en radianes: '+str(lon1))
print('latitud en t2 radianes: '+str(lat2))
print('longitud en g2 radianes: '+str(lon2))


distancia= 6371.01*math.acos(math.sin(lat1)*math.sin(lon1)+math.cos(lat1)*math.cos(lon1)*math.cos(lat2-lon2))
print('la distancia entre los dos puntos es: ' + str(distancia))




