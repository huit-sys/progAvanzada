# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 19:42:56 2019

@author: stitch
"""

año=int(input('Ingresa tu año: '))

if año%12==8:
    animal="Dragon"
elif año%12==9:
    animal='Serpiente'
elif año%12==10:
    animal='caballo'
elif año%12==11:
    animal='oveja'
elif año%12==0:
    animal='mono'
elif año%12==1:
    animal='gallo'
elif año%12==2:
    animal='perro'
elif año%12==3:
    animal='Cerdo'
elif año%12==4:
    animal='Rata'
elif año%12==5:
    animal='buey'
elif año%12==6:
    animal='tigre'
elif año%12==7:
    animal='liebre'
    
print("%d Es el año del %s" % (año,animal))
    
    