# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 00:41:52 2019

@author: stitch
"""

numero1=int(input('ingrese el primer numero entero: '))
numero2=int(input('ingrese el segundo numero entero: '))
numero3=int(input('ingrese el tercer numero entero: '))

mn= min(numero1,numero2,numero3)
mx= max(numero1,numero2,numero3)

md=numero1+numero2+numero3-mn-mx

print('Los numeros en orden son:')
print('',mn)
print('',md)
print('',mx)