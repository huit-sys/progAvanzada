#Un vendedor de una pagina de abarrotes en linea vende dos tipos de cajas de cereal.
#CornFlakes de 750gr y Trix de 500gr. Escriba un programa que lea el numero de cajas 
#de CornFlakes y cajas de Trix, cuyo valor debe ser introducido por el usuario.
# Despues, su programa debe calcular y mostrar
#el total del peso (en kilogramos)
T=500
C=750
Trix=int(input('Cuantas cajas de cereal Trix tiene'))
CornFlakes=int(input('Cuantas cajas de cereal CornFlakes tiene'))

Peso=(Trix*T+CornFlakes*C)//1000

print('El peso en Kilogramos es de',Peso,'kg')
