

#Crear un programa que le pida al usuario la duracion en dias, horas, minutos y segundos. Calcular y desplegar
#la cantidad total de segundos de duracion.

dias=int(input('Introduce el numero de dias'))
horas=int(input('Introduce el numero de horas'))
minutos=int(input('Introduce el numero de minutos'))
segundos=int(input('Introduce el numero de segundos'))

dia=dias*86400
hora=horas*3600
minuto=minutos*60

total=dia+hora+minuto+segundos

print('el tiempo tatal en segundos es',total,'seg')