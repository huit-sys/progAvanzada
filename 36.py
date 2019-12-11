# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 11:13:47 2019

@author: stitch
"""
letra=input('Ingresa una letra: ')
if letra=='a' or letra == 'e' or letra=='i' or letra=='o' or letra =='u':
    print('La letra que escogiste es una vocal')
elif letra=='y':
    print('A veces es una vovcal y a veces es una consonante')
else:
    print('Es una consonante')