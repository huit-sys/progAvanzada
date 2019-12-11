# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 10:05:08 2019

@author: stitch
"""

Toonie=200
Loonie=100
quarter=25
dime=10
nickel=5

centavos=int(input('ingrese los centavos: '))

print("", centavos // Toonie,  'Toonies')
centavos=centavos%Toonie

print("", centavos // Loonie,  'Loonies')
centavos=centavos%Loonie

print("", centavos // quarter,  'quarters')
centavos=centavos%Toonie

print("", centavos // dime,  'dimes')
centavos=centavos%dime

print("", centavos // nickel,  'nickels')
centavos=centavos%nickel

