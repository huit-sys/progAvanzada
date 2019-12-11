# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 22:05:53 2019

@author: stitch
"""

longitud=(float(input('Ingrese la longitud de onda: ')))

if longitud==380 or longitud<450:
    print("Esta longitud de onda pertenece al color violeta")
elif longitud==450 or longitud<495:
    print("Esta longitud de onda pertenece al color Azul")
elif longitud==495 or longitud<570:
    print("Esta longitud de onda pertenece al color verde")
elif longitud==570 or longitud<590:
    print("Esta longitud de onda pertenece al color Amarillo")
elif longitud==590 or longitud<620:
    print("Esta longitud de onda pertenece al color Naranja")
elif longitud==620 or longitud<750:
    print("Esta longitud de onda pertenece al color Rojo")
else:
    print("Esta longitud no corresponde a ningun color")