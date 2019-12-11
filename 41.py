# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 19:18:21 2019

@author: stitch
"""

c4=261.83
d4=293.66
e4=329.63
f4=349.23
g4=392.00
a4=440.00
b4=493.88

nombre=input('Ingrese el nombre de la nota en dos caracteres: ')
nota=nombre[0]
octava=int(nombre[1])

if nota=="c":
    frecuencia=c4
elif nota=="d":
    frecuencia=d4
elif nota=="e":
    frecuencia=e4
elif nota=="f":
    frecuencia=g4
elif nota=="a":
    frecuencia=a4
elif nota=="b":
    frecuencia=b4
    
frecuencia=frecuencia/2**(4-octava)

print('La frecuancia es',nombre, "es",frecuencia)



    

    

    

