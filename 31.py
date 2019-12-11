# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 00:17:37 2019

@author: stitch
"""
n=int(input('Introduce cuatro digitos: '))

f1=n//100
f2=(n%100)//10
f3=(n%100)%10

suma=f1+f2+f3

print('la suma de los numeros es:', str(suma))




