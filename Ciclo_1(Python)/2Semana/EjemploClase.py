# -*- coding: utf-8 -*-
"""
Created on Sat May 29 10:26:39 2021

@author: estusaee2
"""
numeros_negativos = 0
rango = int(input("Cantidad de datos a ingresar: "))

for i in range(0,rango,1):
    numero = int(input(f"Ingrese el dato {i+1} de {rango}: "))
    
    if numero < 0 :
        numeros_negativos += 1
        
print(f"Usted ingresó {numeros_negativos} numeros negativos") 