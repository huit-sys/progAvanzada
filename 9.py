#Interes compuesto
#Usted acaba de abri una nueva cuenta de ahorro con el cual gana el 4% de interes por año. 
#El interes que usted genera es pagado al fin del año, y es agregado al balance de la cuenta de banco.
#Escriba un programa ue comience por leer la cantidad de dinero depositada en la cuenta 
#(el usuario introduce esta cantidad). El programa debe de calcular y mostrar la cantidad
# de dinero en la cuenta despues del prime, segundo y tercer año. Despliege las cantidades
#de dinero redondeando a 2 decimales

cantidad=int(input('El usuario introduce esta cantidad'))
priAño=(cantidad/100)*4+cantidad
segAño=(priAño/100)*4+priAño
terAño=(segAño/100)*4+segAño

print('El interes del primer año es de $%.2f' % priAño)
print('El interes del segundo año es de $%.2f' % segAño)
print('El interes del tercer año es de $%.2f' % terAño)


