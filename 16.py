# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 11:34:06 2019

@author: stitch
"""
import math
radio=int(input('ingrese el radio: '))

area=math.pi*radio**2
volumen=(4/3)*math.pi*radio**3

print('el area del circulo es: ',str(area))
print('el volumen del circulo es: ',str(volumen))