# -*- coding: utf-8 -*-
"""
Created on Thu May 27 19:15:54 2021

@author: nick_
"""

print("SELECCIÓN DE PIZZA")
print("Todas nuestras pizzas tienen Tomate y Queso como ingredientes básicos")
print("Vegetariana: 1", "\nNo vegetariana: 2")
pizza = int(input("¿Cómo quiere su pizza?: "))
if pizza == 1: 
    print("Escoja los ingredientes para su pizza vegetariana separados por coma: \n- Pimiento: p\n- Tofu: t")
    ingredientes_veg = input("Ingredientes: ")
    if ingredientes_veg == "p, t":
        print("Su pizza vegetariana tendrá Pimientos y Tofu.")
    elif ingredientes_veg == "p":
        print("Su pizza vegetariana traerá sólo Pimientos además de los ingredientes básicos.")
    elif ingredientes_veg == "t":
        print("Su pizza vegetariana traerá sólo Tofu además de los ingredientes básicos.")
    
else: 
    
    print("Escoja los ingredientes para su pizza separados por coma: \n- Peperoni: pe\n- Jamón: j\n- Salmón: s")
    ingredientes_no_veg = input("Ingredientes: ")
    if ingredientes_no_veg == "pe, j, s":
        print("Su pizza tendrá Peperoni, Jamón y Tofu, además de los ingredientes básicos.")
    elif ingredientes_no_veg == "pe, j":
        print("Su pizza traerá Peperoni y Jamón, además de los ingredientes básicos.")
    elif ingredientes_no_veg == "pe, s":
        print("Su pizza traerá Peperoni y Salmón, además de los ingredientes básicos.")
    elif ingredientes_no_veg == "j, s":
        print("Su pizza traerá Jamón y Salmón, además de los ingredientes básicos.")
    elif ingredientes_no_veg == "j":
        print("Su pizza traerá solo Jamón, además de los ingredientes básicos.")
    elif ingredientes_no_veg == "s":
        print("Su pizza traerá sólo Salmón, además de los ingredientes básicos.")
    elif ingredientes_no_veg == "pe":
        print("Su pizza traerá sólo Peperoni, además de los ingredientes básicos.")