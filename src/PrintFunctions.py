# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 22:13:39 2021

@author: David
"""

def printMessage( *message,  delimiter = None, matrix = None):
    if delimiter != None:
        print(delimiter)
    for mes in message:
        if matrix != None: # si es una matriz que la muestre con forma
            for mat in mes:
                print(mat)
        else:               # si no es matriz que muestre los argumentos
            print(mes)
    if delimiter != None:
        print(delimiter)




