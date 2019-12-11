# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 12:00:35 2019

@author: stitch
"""
import math
radio=float(input('ingrese el radio del cilindro: '))
altura=float(input('ingrese la altura del cilindro: '))

volumen=(math.pi*radio**2)*(altura)

print('el volumen del cilindro es: %.1f'%volumen)
