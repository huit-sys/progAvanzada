# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 18:10:22 2019

@author: stitch
"""
deno=float(input('Escriba una denominacion de billete en dolares: '))

if deno==1:
    input('En este billete aparece George Washington')
elif deno==2:
    input('En este billete aparece Tomas Jefferson')
elif deno==5:
    input('En este billete aparece Abraham Lincoln')
elif deno==10:
    input('En este billete aparece Alexander Hamilton')
elif deno==20:
    input('En este billete aparece Andrew Jackson')
elif deno==50:
    input('En este billete aparece Ulysses S. Grant')
elif deno==100:
    input('En este billete aparece Benjamin Franklin')
else:
    input('La denominacion que inserto no existe, intente de nuevo')
