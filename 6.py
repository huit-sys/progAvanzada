# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 15:08:48 2019

@author: stitch
"""

#hacer un progrmaa en el que el ussuario introduzca el nombre de la comida que ordeno
#en un restaurante y su precio. despues, su programa debe calcular el subtotal, el iva,
#y la propina de toda la cuenta. La salida del programa dee parecerse a un ticket de restaurante.
#use un iva del 16% y una propina del 15% del subtotal. Los valores numericos deben tener dos decimales
A= str(input('introduzca el nombre de la comida: ')) 
a= float(input('introduzca el valor de la comida: ')) 

B= str(input('introduzca el nombre de la comida: ')) 
b= float(input('introduzca el valor de la comida: ')) 

C= str(input('introduzca el nombre de la comida: ')) 
c= float(input('introduzca el valor de la comida: ')) 

D= str(input('introduzca el nombre de la comida: ')) 
d= float(input('introduzca el valor de la comida: ')) 

E= str(input('introduzca el nombre de la comida: ')) 
e= float(input('introduzca el valor de la comida: ')) 


print('Platillo1: ' + A)
print('Platillo2: ' + B)
print('Platillo3: ' + C)
print('Platillo4: ' + D)
print('Platillo5: ' + E)





print('-------------------')
subtotal=a+b+c+d+e
print('subtotal: $%.2f ' % subtotal)
iva=subtotal*0.16
print('iva: $%.2f ' % iva)
propina= subtotal*0.15
print('propina: $%.2f '% propina)

print('-------------------')
print('       total')
print('-------------------')
total=subtotal+iva+propina
print('total: $%.2f' % total)
