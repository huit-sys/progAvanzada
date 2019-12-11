# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 20:01:57 2019

@author: stitch
"""

factor=2400.00
inaceptable=0
aceptable=0.4
merecedor=0.6

radio=float(input("Ingresa el radio: "))

if radio==inaceptable:
    performance="inaceptable"
elif radio==aceptable:
    performance="merecedor"
elif radio>= merecedor:
    performance="merecedor"
else:
    performance=""
    
if performance=="":
    print("Has ingresador un radio erroneo")
else:
    print("basado en la calificacion, el rendimiento es %s:" %performance)
    print("Recibiras un aumento de $%.2f"%(radio*factor))
    