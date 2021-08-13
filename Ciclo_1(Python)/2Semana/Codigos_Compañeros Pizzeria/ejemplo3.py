# -*- coding: utf-8 -*-
"""
Created on Thu May 27 18:43:37 2021

@author: santiago

Programa de pizza
"""

Menu= int(input("Bienvenidos a la pizzeria, elija el tipo de pizza, marque 1 para Vegetariana, 2 para Normal: "))

if Menu==1:
    vegetariano=["1-Pimiento","2-Tofu"]
    ingrediente=int(input( f"Escoga los ingredientes {vegetariano}: "))
    try:
        pizza=vegetariano[ingrediente-1]
        print(f"Su pizza es de {pizza}")
    except:
        print("Eleccion fuera del menu")
elif Menu==2:
    normal=["1-Peperoni","2-Jamon","3-Salmon"]
    ingrediente=int(input( f"Escoga los ingredientes {normal}: "))
    try:
        pizza=normal[ingrediente-1]
        print(f"Su pizza es de {pizza}")
    except:
        print("Eleccion fuera del menu")
else:
    print("Tu eleccion no esta dentro del menu")
