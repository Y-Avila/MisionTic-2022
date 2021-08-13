# -*- coding: utf-8 -*-
"""
Created on Thu May 27 18:01:57 2021

@author: jsbarriosm@unal.edu.co
"""

tipo_pizza = int (input ("¿qué tipo de pizza deseas (1 = Vegetariana, 2 = No Vegetariana)? "))

if tipo_pizza != 1 and tipo_pizza != 2:
    print ("La opción no es válida. Por favor intente de nuevo.")
elif tipo_pizza == 1:
    print ("Puedes escoger entre Pimiento y Tofu.")
    ingrediente = int (input ("¿qué ingrediente deseas (1 = Pimiento, 2 = Tofu)?"))
    if ingrediente == 1:
        print ("Tu pizza vegetariana con Pimiento, Queso Mozarrella y Tomate estará lista en 10 minutos.")
    elif ingrediente == 2:
        print ("Tu pizza vegetariana con Tofu, Queso Mozarrella y Tomate estará lista en 10 minutos.")
    else:
        print ("La opción no es válida. Por favor intente de nuevo.")
else:
    print ("Puede escoger entre Pepperoni, Jamón o Salmón.")
    ingrediente = int (input ("¿qué ingrediente deseas (1 = Pepperoni, 2 = Jamón, 3 = Salmón)?"))
    if ingrediente == 1:
        print ("Tu pizza no vegetariana con Pepperoni, Queso Mozarrella y Tomate estará lista en 10 minutos.")
    elif ingrediente == 2:
        print ("Tu pizza no vegetariana con Jamón, Queso Mozarrella y Tomate estará lista en 10 minutos.")
    elif ingrediente == 3:
        print ("Tu pizza no vegetariana con Salmón, Queso Mozarrella y Tomate estará lista en 10 minutos.")
    else:
        print ("La opción no es válida. Por favor intente de nuevo.")