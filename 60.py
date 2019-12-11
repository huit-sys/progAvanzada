# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 15:35:15 2019

@author: stitch
"""

from random import randrange

valor=randrange(0,38)
if valor==37:
    print("El giro resulto en 00...")
else: 
    print("El giro resulto en %d..." %valor)
if valor==37:
    print("paga 00")
else:
    print("paga", valor)
    
if valor%2==1 and valor>=1 and valor<=9 or\
   valor%2==0 and valor>=12 and valor<=18 or\
   valor%2==1 and valor>=19 and valor<=27 or\
   valor%2==0 and valor>=30 and valor<=36:
       print("pagar rojo")
elif valor==0 or valor==37:
    pass
else:
    print("Pagar negro")
if valor>=11 and valor<=36:
    if valor%2==1:
        print("paga impar")
    else:
        print("Paga incluso")
if valor>=1 and valor<=18:
    print("paga 1 a 18")
elif valor>=19 and valor<=36:
    print("paga 19 a 36")