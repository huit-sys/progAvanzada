# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 19:51:29 2019

@author: stitch
"""

c4=261.83
d4=293.66
e4=329.63
f4=349.23
g4=392.00
a4=440.00
b4=493.88
limite=1

frecuencia=float(input('Ingrese la frecuencia: '))

if frecuencia>=c4-limite and frecuencia<=c4+limite:
    nota="c4"
elif frecuencia >=d4-limite and frecuencia<=d4+limite:
    nota="d4"
elif frecuencia>=f4-limite and frecuencia<=f4+limite:
    nota="f4"
elif frecuencia>=g4-limite and frecuencia<=g4+limite:
    nota="g4"
elif frecuencia >=a4-limite and frecuencia<=a4+limite:
    nota="a4"
elif frecuencia>=b4-limite and frecuencia<=b4+limite:
    nota="b4"
else:
    nota=""
    
if nota=="":
    print('No se encuentra una nota que corresponda a esa frecuencia')
else: 
    print('La frecuancia corresponde a la nota', nota)
    