# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 20:21:51 2019

@author: stitch
"""


temp=int(input('Introduce la temperatura del aire: '))
vel=int(input('Introduce la velocidad del viento: '))

wci=13.2+0.6215*temp-11.37*vel**0.16+0.3965*temp**0.16

print('la sensacion termica indice es: ', round(wci))
