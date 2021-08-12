#Operaciones arimeticas y concatenaciones de cadena de texto para mostrar en 
#pantalla los resultados

#Comentar algunas secciones del codigo para almacenar la informacion, pero
#Usar solo las operaciones necesarias.


# Problema 1 
"""
numero1 = input("Digite el primer numero ")
numero2 = input("Digite el segundo numero ")
promedio = (int(numero1) + int(numero2))/ 2
print("El promedio es ",promedio)
"""

# Problema 2
"""
peso = float(input("Digite su peso en kilogramos "))
altura = float(input("Digite su altura en metros "))
imc = round(peso/altura**2,2)
print(imc)
"""
# Problema 3
"""
distanciap = float(input("Digite distancia en pulgadas "))
centimetros = distanciap*2.54
print(centimetros)
"""
#Problema 4
"""
distanciapies = float(input("Digite distancia en pies "))
centimetros = (distanciapies*12)*2.54
print(centimetros)
"""
#Problema5
distanciapies = 14
distanciapulgadas = 12
centimetros = (distanciapies*12)*2.54 + distanciapulgadas*2.54
print(round(centimetros,10))
