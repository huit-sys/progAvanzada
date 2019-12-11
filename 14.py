# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 11:10:27 2019

@author: stitch
"""

pies=int(input('ingrese el numero de pies: '))
pulgadas=int(input('ingrese el numero de pulgadas: '))

pies2=pies*(1/0.0328084)
pul2=pulgadas*((25.4/1)*(1/10))

print('la altura de pies a centimetros es:'+str(pies2),'cm')
print('la altura de pulgadas a centimetros es:'+str(pul2),'cm')
