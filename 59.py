# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 14:10:58 2019

@author: stitch
"""

matricula=input('Ingresa la matricula: ')
if len(matricula)==6 and matricula[0]>="A" and matricula[0]<="Z" and\
matricula[1]>="A" and matricula[1]<="Z" and\
matricula[2]>="A" and matricula[2]<="Z" and\
matricula[3]>="0" and matricula[3]<="9" and\
matricula[4]>="0" and matricula[4]<="9" and\
matricula[5]>="0" and matricula[5]<="9":
    print('La matricula es antigua y valida')
elif len(matricula)==7 and matricula[0]>="0" and matricula[0]<="9" and\
matricula[1]>="0" and matricula[1]<="9" and\
matricula[2]>="0" and matricula[2]<="9" and\
matricula[3]>="0" and matricula[3]<="9" and\
matricula[4]>="A" and matricula[4]<="Z" and\
matricula[5]>="A" and matricula[5]<="Z" and\
matricula[6]>="A" and matricula[6]<="Z":
    print("La placa es de estilo nuevo y valida")
else:
    print("La matricula no es valida")