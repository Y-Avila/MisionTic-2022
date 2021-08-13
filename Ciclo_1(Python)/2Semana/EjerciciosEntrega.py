#  EJERCICIO 1
"""
Elabore un programa en Python que lea una temperatura en grados Celsius,
la convierta a grados Kelvin y muestre el resultado con un mensaje bien 
explicativo. No use aproximaciones

temperatura_celcius = float(input("Digite una temperatura en grados Celsius "))    
temperatura_kelvin = temperatura_celcius + 273.15
mensaje = f"{temperatura_celcius} grados Celcius corresponden a"
print(mensaje,temperatura_kelvin,"grados Kelvin")
"""
#  EJERCICIO 2
"""
Elabore un programa en Python que lea un entero de dos dígitos y produzca 
como salida los dígitos del número leído con su correspondiente mensaje. 
Por ejemplo, si el número leído es 27, la salida deberá ser:
(sin texto adicional):
2
7

entero = "1"
while len(entero) != 2:
    entero = input("Digite un entero de dos digitos: ")    
print(entero[0],entero[1],sep="\n")
"""
#  EJERCICIO 3
"""
Elabore programa en Python que lea dos datos enteros correspondientes a 
los catetos de un triángulo rectángulo y que calcule e imprima el valor de
 la hipotenusa de dicho triángulo.

cateto_adyacente = int(input("Digite el valor entero del cateto adyacente: "))
catero_opuesto =int(input("Digite el valor entero del cateto opuesto: "))
hipotenusa = (cateto_adyacente**2 + catero_opuesto**2)**(1/2)
print(hipotenusa)
 """ 
#  EJERCICIO 4
"""
Elabore programa en Python que le permita al usuario ingresar números enteros 
de manera indefinida, hasta que ingrese un número negativo, y al final 
imprimir la suma de los números enteros pares sin incluir el número negativo
 en la suma.
"""
lista =[]
elemento = 0
numero = 1
suma = 0
while numero >= 0 :
    numero = int(input("Ingrese un numero entero: "))
  
    if numero%2 == 0 and numero >= 0 :
        lista.append(numero)
        elemento = elemento + 1

for i in range(0,elemento,1):
    suma = suma + lista[i]
 
  
print(suma)
        


