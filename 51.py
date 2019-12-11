# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 11:25:26 2019

@author: stitch
"""

A=4.0
A_MINUS=3.7
B_PLUS=3.3
B=3.0
B_MINUS=2.7
C_PLUS=2.3
C=2.0
C_MINUS=1.7
D_PLUS=1.3
D=1.0
F=0
invalido=-1

letra=input('Ingresa la calificacion en letra: ')
letra=letra.upper()
if letra=="A+" or letra=="A":
    gp=A
elif letra=="A-":
    gp= A_MINUS
elif letra=="B+":
    gp =B_PLUS
elif letra=="B":
    gp =B
elif  letra=="B-":
    gp=B_MINUS
elif letra=="C":
    gp=C
elif letra=="C-":
    gp =C_MINUS
elif letra=="D+":
    gp = D_PLUS
elif letra=="D":
    gp=D
elif letra=="F":
    gp=F
else:
    gp=invalido
    
if gp==invalido:
    print("La calificacion no existe")
else: 
    print("La calificacion es ", gp)
    