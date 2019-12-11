
#Ejercicio 11. Eficiencia de combustible
#En los Estados Unidos, la eficiencia del combustible para vehículos se expresa 
#normalmente en millas por galón (MPG). En México, la eficiencia del combustible 
#normalmente se expresa en litros por cien kilómetros (L / 100km).
#Usa tus habilidades de investigación para determinar cómo convertir de MPG a L / 100km. 
#Luego, cree un programa que lea un valor del usuario en unidades estadounidenses 
#y muestre la eficiencia de combustible equivalente en unidades mexicanas.

mille=1.609
gall=3.78

a=int(input('Introduce el valor en MPG'))

conversion=(a*mille)/gall

print('El valor en unidades mexicanas es de %.2f' % conversion,'Litros por cien kilometros')

