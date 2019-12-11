#En muchos, se agrega un pequeño depósito a los envases de bebidas para alentar a las personas a reciclarlos. En una jurisdicción en particular, los envases de bebidas con un litro o menos tienen un depósito de $ 0.10, y los envases de bebidas con más de un litro tienen un depósito de $ 0.25
#Escriba un programa que lea el número de contenedores de cada tamaño del usuario. Su programa debe continuar calculando y mostrando el reembolso que se recibirá por devolver esos contenedores. Formatee la salida para que incluya un signo de dólar y siempre muestre exactamente dos decimales.
a=0.10
b=0.25
Botella1=int(input('Cuantas botellas chicas va a ingresar'))
Botella2=int(input('Cuantas botellas grandes va a ingresar'))
Operacion=Botella1*a + Botella2*b

print('Tu rembolso es de $%.2f' % Operacion)




