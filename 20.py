##Ejercicio 20
##La ley de los gases ideales es una aproximación matemática del comportamiento de los gases como
##cambio de presión, volumen y temperatura. Por lo general, se indica como:
##PV = nRT
##donde P es la presión en Pascales, V es el volumen en litros, n es la cantidad de
##sustancia en moles, R es la constante de gas ideal, igual a 8.314 J/mol K, y T es el temperatura en grados Kelvin.
##Escriba un programa que calcule la cantidad de gas en moles cuando el usuario suministra
##La presión, el volumen y la temperatura. Prueba tu programa determinando el número de moles de gas en un tanque de buceo.
##Un tanque de buceo típico contiene 12 litros de gas a una presión de 20,000,000 Pascales (aproximadamente 3,000 PSI).
## La temperatura ambiente es aproximadamente 20 grados Celsius o 68 grados Fahrenheit.

P=20000000
R=8.314
V=12
T=20
nmoles=int(input('Introduce el numero de moles'))
moles=(P*V)/(R*T)
print('el número de moles de gas en un tanque de buceo es de',moles)
