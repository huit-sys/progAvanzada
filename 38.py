# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 11:43:01 2019

@author: stitch
"""

mes=input('Ingresa el nombre del mes: ')
dias=31
if mes=='abril' or mes=='junio' or mes=='septiembre' or mes=='Noviembre':
    dias =30
elif mes== 'febrero':
    dias='28 o 29'
    
print(mes, 'tiene',dias,'dias' )

