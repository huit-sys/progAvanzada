# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 14:36:51 2019

@author: stitch
"""

#ejersicio34
#Escriba un programa que lea un numero entero inreoducido por el usuario. Su
#programa debe desplegar un mensaje indicando si es un numero entero es par o impar.

num=int(input('Inserta un nuemero entero: '))

if(num%2==0):
 print(str(num)+" es par")
else:
 print(str(num)+" es impar")
