# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 17:08:44 2019

@author: stitch
"""
#martillo neumatico----130 db
#cortacesped a gas----106 db
#despertador----------70 db
#cuarto tranquilo------40 db
deci=float(input('Ingrese el nivel de ruido en decibelios: '))

if deci==40:
    input('El ruido corresponde al de un cuarto tranquilo' )
elif deci==70:
    input('El ruido corresponde a un despertador')
elif deci==106:
    input('El ruido corresponde a un cortacesped a gas')
elif deci==130:
    input('El ruido corresponde a un martillo neumatico')
elif deci >0 and deci==40:
    input('El ruido corresponde al de un cuarto tranquilo' )
elif deci>40 and deci<70:
    input('El ruido esta entre los niveles de un cuarto tranquilo y un despertador')
elif deci>70 and deci<106:
    print('El ruido esta entre los niveles de un despertador y un cortacesped a gas' )
elif deci>106 and deci<130:
    input('El ruido esta entre los niveles de un cortacesped a gas y un martillo neumatico')
elif deci>=130:
    input('El ruido correspnde a un martillo neumatico')
else:
    input('Error, ingrese un numero valido')
    


