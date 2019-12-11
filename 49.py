# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 09:17:21 2019

@author: stitch
"""

mag=float(input('Ingresa la magnitud: '))

if mag==2.0:
    print('un terremoto de agnitud ',mag,' se considera micro')
elif mag>2.0 and mag<=3.0:
    print('un terremoto de agnitud ',mag,' se considera muy menor')
elif mag>3.0 and mag <=4.0:
    print('un terremoto de agnitud ',mag,' se considera  menor')
elif mag>4.0 and mag <=5.0:
    print('un terremoto de agnitud ',mag,' se considera ligero')
elif mag>5.0 and mag<=6.0:
    print('un terremoto de agnitud ',mag,' se considera moderado')
elif mag>6.0 and mag<=7.0:
    print('un terremoto de agnitud ',mag,' se considera fuerte')
elif mag>7.0 and mag<=8.0:
    print('un terremoto de agnitud ',mag,' se considera mayor')
elif mag>8.0 and mag<=10.0:
    print('un terremoto de agnitud ',mag,' se considera extremo')
elif mag>10:
    print('un terremoto de agnitud ',mag,' se considera meteorico')
else:
    print('Error')
    
    
    
    
    


