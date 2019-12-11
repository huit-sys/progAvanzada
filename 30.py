# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 00:00:47 2019

@author: stitch
"""

kpa=int(input('Introduce la presion en kpa: '))

pas=kpa*(1000/1)
lb=pas*(1/4.4482)*(1/1550)

atm=(kpa/1)*(1/101.3)

print('La presion de kpa en lb por in cuadradas es de:',str(lb))
print('La presion en kpa a atmosferas es de:',str(atm))


