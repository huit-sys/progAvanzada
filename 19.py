# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 14:23:34 2019

@author: stitch
"""

#Ejersicio 19
#Escriba un programa que determine como un objeto viaja cuando golpea el piso
#El usuario insertara la informacion de la altura desde donde el objeto se dejara caeer,
#en metros (m). Dado que el onjeto se deja caer desde reposo (velocidad inicial 
# V0=0 m/s). Asumiendo que la aceleracion debido a la gravedad es p.81 m/s **2 y 
#usando la formula Vf=raiz(Vo**2+2gd), calcule la velocidad final vf usando la
#velocidad inicial vo, la aceleracion g, y la distancia d.


import math

dis=int(input("ingresa la distancia: "))
gravedad=9.81
inicial=0

final=math.sqrt(0**2+2*(gravedad)*(dis))
print('la distancia es: ' + str(final))


