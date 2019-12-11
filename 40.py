# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 19:09:40 2019

@author: stitch
"""

l1=float(input('Ingrese la primer Longitud; '))
l2=float(input('Ingrese la segunda Longitud; '))
l3=float(input('Ingrese la tercer Longitud; '))

if l1==l2==l3:
    input('Se trata de un triangulo equlatero')
elif l1==l2 or l1==l2 or l2==l3:
    input('Se trata de un Triangulo isoceles')
else: 
    input('Se trata de un triangulo escaleno')