# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 15:21:55 2019

@author: stitch
"""

largo= float(input('cual es largo del campo en metros: ')) 

ancho= float(input('cual es ancho de la habitacion: '))

area= (largo * ancho )*(1.0/4046.86)


print('el area es: ' + str(area),('acres'))
