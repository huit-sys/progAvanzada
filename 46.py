# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 15:25:44 2019

@author: stitch
"""

#ejersicio46... El año esta dividido en cuatro temporadas: primaera,verano, otoño e
#invierno, usemos las siguientes fechas
#temporada de primer dia
#-----------------------
#primavera marzo21
#verano junio 21
#otoño septiembre 22
#invierno Diciembre 21

mes=str(input('inserta el mes: '))
dia=int(input('inserta el dia: '))

if mes =="enero" or mes=="febrero":
  temporada="invierno"
elif mes=="marzo":
  if dia<20:
    temporada=="invierno"
  else:
    temporada=="primavera"
elif mes=="abril" or mes=="mayo":
  temporada=="primavera"
elif mes=="junio":
  if dia<21:
    temporada=="primavera"
else:
  temporada=="verano"
elif mes=="julio" or mes=="agosto":
  temporada="verano"
elif mes=="septiembre":
  if dia<22:
    temporada="verano"
  else:
    temporada ="otoño"
elif mes=="octubre" or mes=="noviembre":
  temporada="otoño"
elif mes=="diciembre":
  if dia<21:
    temporada="otoño"
                
else:
    temporada="inverno"
                
    print(mes, dia, "es en", temporada)
    
    
        
        

