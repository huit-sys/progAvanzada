# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 17:57:48 2019

@author: stitch
"""

rad=float(input('Ingrese la frecuencia de la radiacion(Hz): '))


if rad<3*10**9:
    print("Esta frecuencia corresponde a ondas de radio")
elif rad==3*10**9 or rad<3*10**12:
    print("Esta frecuencia corresponde a microondas")
elif rad==3*10**12 or rad<4.3*10**14:
    print("Esta frecuencia corresponde a luz infraroja")
elif rad==4.3*10**14 or rad<7.5*10**14:
    print("Esta frecuencia corresponde a luz visible")
elif rad==7.5*10**14 or rad<3*10**17:
    print("Esta frecuencia corresponde a luz ultravioleta")
elif rad==3*10**17 or rad<3*10**19:
    print("Esta frecuencia corresponde a rayos-x")
elif rad==3*10**19 or rad>3*10**19:
    print("Esta frecuencia corresponde a rayos gamma")
    