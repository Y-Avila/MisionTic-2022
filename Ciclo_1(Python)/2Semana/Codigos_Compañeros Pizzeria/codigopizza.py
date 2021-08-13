# -*- coding: utf-8 -*-
"""
Created on Thu May 27 18:44:44 2021

@author: pc
"""

tipo_de_pizza = int(input("Escoja 1 si su pizza es vegetariana y 2 si no es vejetariana "))

if tipo_de_pizza == 1:
    ingrediente_vegetariano = int(input("escoja 1 para pimiento y 2 para tofu "))
    if ingrediente_vegetariano == 1:
        print("su tipo de pizza es vegetariana y los ingredientes son pimiento, mozzarela y tomate")
    elif ingrediente_vegetariano ==2:
        print("su tipo de pizza es vegetariana y los ingredientes son tofu, mozzarela y tomate")
    else:
        print("ingrese un valor valido")
elif tipo_de_pizza == 2:
    ingrediente_no_vegetariano = int(input("escoja 1 para peperoni, 2 para jamon y 3 para salmon "))
    if ingrediente_no_vegetariano == 1:
        print("su tipo de pizza es no vegetariana y los ingredientes son peperoni, mozzarela y tomate")
    elif ingrediente_no_vegetariano == 2:
        print("su tipo de pizza es no vegetariana y los ingredientes son jamon, mozzarela y tomate")
    elif ingrediente_no_vegetariano == 3:
        print("su tipo de pizza es no vegetariana y los ingredientes son salmon, mozzarela y tomate")
    else:
        print("ingrese un valor valido")
else:
    print("escriba una opción valida")