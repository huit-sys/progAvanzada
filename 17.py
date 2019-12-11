# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 11:44:08 2019

@author: stitch
"""
import math
capagua=4.186
elec=8.9
kwh=2777*math.e**-7

volumen=float(input('ingrese la cantidad de agua: '))
temp=float(input('ingrese la tempreatura: '))

q=volumen*temp*capagua

print('Este requiere %d Joules de energia' %q)

kilo=q+kwh
cost=kilo+8.9
print('Este es el costo de la anergia: %.2f' %cost)

