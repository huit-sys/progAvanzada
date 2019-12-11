# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 09:49:18 2019

@author: stitch
"""

import math

num1=int(input("Ingrese el valor de a: "))
num2=int(input("Ingrese el valor de b: "))

suma=num1+num2
producto=num1*num2
cociente=math.floor(num1/num2)
residuo=num1%num2
loga=math.log(num1)
pot=num1**num2

print('la suma de los numeros es: '+str(suma))
print('el producto de los numeros es: '+str(producto))
print('el cociente de los numeros es: '+str(cociente))
print('el residuo de los numeros es: '+str(residuo))
print('el residuo es: '+str(residuo))
print('el logaritmo de a es: '+str(loga))
print('la potencia de a elevado a b es: '+str(pot))
