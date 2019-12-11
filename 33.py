# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 00:54:25 2019

@author: stitch
"""

prec=3.49
desc=0.60

num=int(input('ingrese el numero de panesen un dia: '))

reg=num*prec
descuento=reg*desc
total=reg-descuento

print('precio regular: %5.2f' %reg)
print('descuento: %5.2f' %descuento)
print('total: %5.2f' % total)