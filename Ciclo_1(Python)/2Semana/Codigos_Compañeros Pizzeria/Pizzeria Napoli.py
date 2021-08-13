# -*- coding: utf-8 -*-
"""
Created on Thu May 27 18:43:30 2021

@author: DiegoMoreno
"""



tipo_pizza= str(input("Bienvenido a Bella Napoli, tenemos pizas vegetariana y No vegetariana, escriba el tipo de pizza como aparece en este mensaje "))


if tipo_pizza == "vegetariana":
    ingrediente= str(input("Seleccione uno de estos ingredientes escribiendolo como aparece aqui: Pimienta; tofu "))
else:
    ingrediente= str(input("Seleccione uno de estos ingredientes escribiendolo como aparece aqui: peperoni, jamon, salmon "))
    
print("Tu seleccion es ", tipo_pizza,"con ", ingrediente, "Mozarella y tomate")