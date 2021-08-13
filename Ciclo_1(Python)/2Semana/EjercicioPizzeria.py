# -*- coding: utf-8 -*-
"""
Created on Thu May 27 18:54:10 2021

@author: estusaee2
"""

# Ejercicio Pizza


preferencia = input("¿Quiere una pizza vegetariana? (Responda con número de acuerdo a la opción) \n 1: Si \n 2: No \n\n")

if preferencia == 1 :
    ingrediente_vegetariano = input("Eliga un ingrediente (Responda con número de acuerdo a la opción) \n 1: Pimiento \n 2: Tofu \n\n")
elif preferencia == 2 :
    ingrediente_no_vegetariano =  input("Eliga un ingrediente (Responda con número de acuerdo a la opción) \n 1: Peperoni \n 2: Jamón \n 3: Salmón \n\n")


if preferencia == 1 :
    preferencia = "Vegetariana"
    
    if ingrediente_vegetariano == 1 :
        ingrediente_vegetariano = "Pimiento"
    elif  ingrediente_vegetariano == 2 :
        ingrediente_vegetariano = "Tofu"
    
elif preferencia == 2:
    preferencia = "No Vegetariana"    
        
    if ingrediente_no_vegetariano == 1 :
        ingrediente_no_vegetariano = "Peperoni"
    elif ingrediente_no_vegetariano == 2 :
        ingrediente_no_vegetariano = "Jamón"
    elif ingrediente_no_vegetariano == 3:
        ingrediente_no_vegetariano = "Salmón"
    
print("Su pedido es una pizza",preferencia,", con los siguientes ingredientes:\n\n - Mozarella (Basico) \n - Tomate (Basico) \n ")