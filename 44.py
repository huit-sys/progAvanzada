# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 18:21:32 2019

@author: stitch
"""

dia=int(input('Ingrese un dia del mes: '))
mes=input('Ingrese el mes: ')

if dia==1 and mes=="enero":
    input('La fecha que eligio es año nuevo')
elif dia==1 and mes=="julio":
    input('La fechaque eligio es dia de Canada')
elif dia==25 and mes=="diciembre":
    input('La fecha que eligio es dia de navidad')
else: 
    input('Este mes y dia no corresponen a un dia festivo de las fechas fijadas')