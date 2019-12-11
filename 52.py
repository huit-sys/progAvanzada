# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 18:33:13 2019

@author: stitch
"""





aa="A"
a="A-"
bb="B+"
B="B"
b="B-"
cc="C+"
C="C"
c="C-"
dd="D+"
d="D"
f="F"
invalid="invalida"


calificacion=float(input('Ingresa la calificación: '))
if calificacion==0.0 or calificacion<1.0:
    gp=f
elif calificacion==1.0 or calificacion<1.3:
    gp= d
elif calificacion==1.3 or calificacion<1.7:
    gp =dd
elif calificacion==1.7 or calificacion<2.0:
    gp =c
elif calificacion==2.0 or calificacion<2.3:
    gp=C
elif calificacion==2.3 or calificacion<2.7:
    gp=cc
elif calificacion==2.7 or calificacion<3.0:
    gp =b
elif calificacion==3.0 or calificacion<3.3:
    gp = B
elif calificacion==3.3 or calificacion<3.7:
    gp=bb
elif calificacion==3.7 or calificacion<4.0:
    gp=a
elif calificacion==4.0:
    gp=aa
else:
    gp=invalid
    
print("La calificacion es ", gp)
    