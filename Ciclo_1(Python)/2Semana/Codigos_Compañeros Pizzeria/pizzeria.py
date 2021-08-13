ingredientes_obligatorios = "Mozarrella, Tomate"


escoge_tu_pizza = """
Hola, bienvenid@ a pizzería Bella Napoli, la mejor pizza de la ciudad

¿Deseas una pizza vegetariana?

1. Sí
2. No

Responde con un número
"""

eleccion = int(input(escoge_tu_pizza))

if eleccion == 1:
    vegetariana = """
    Excelente elección, la vegetariana es de mis favoritas!
    
    Ahora escoge un ingrediente para acompañar tu pizza
    
    1. Pimiento
    2. Tofu
    
    Responde con un número
    """
    ingrediente_vegetariano = int(input(vegetariana))
    if ingrediente_vegetariano == 1:
        print("La pizza elegida es vegetariana y los ingredientes que lleva son: " + ingredientes_obligatorios + " y Pimiento")
    elif ingrediente_vegetariano == 2:
        print("La pizza elegida es vegetariana y los ingredientes que lleva son: " + ingredientes_obligatorios + " y Tofu")
elif eleccion == 2:
    no_vegetariana = """
    Excelente elección, yo tampoco soy muy fan de la pizza vegetariana :)
    
    Ahora escoge un ingrediente para acompañar tu pizza
    
    1. Peperoni
    2. Jamón
    3. Salmón
    
    Responde con un número
    """
    ingrediente_no_vegetariano = int(input(no_vegetariana))
    if ingrediente_no_vegetariano == 1:
        print("La pizza elegida NO es vegetariana y los ingredientes que lleva son: " + ingredientes_obligatorios + " y Peperoni")
    elif ingrediente_no_vegetariano == 2:
        print("La pizza elegida NO es vegetariana y los ingredientes que lleva son: " + ingredientes_obligatorios + " y Jamón")
    elif ingrediente_no_vegetariano == 3:
        print("La pizza elegida NO es vegetariana y los ingredientes que lleva son: " + ingredientes_obligatorios + " y Salmón")
    else:
        print("Error, tu elección no está dentro del menú de opciones")   
else:
    print("Error, tu elección no está dentro del menú de opciones")