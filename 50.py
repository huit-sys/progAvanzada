# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 09:33:13 2019

@author: stitch
"""
import math
a=float(input('Escriba el valor de a: '))
b=float(input('Escriba el valor de b: '))
c=float(input('Escriba el valor de c: '))

pos=(-b+math.sqrt((b**2)-4*(a*c)))/(2*a)
neg=(-b-math.sqrt((b**2)-4*(a*c)))/(2*a)

input('El valor de la raiz positiva es de: ',str(pos))
input('El valor de la raiz negativa es de: ',str(neg))
