respuesta = int(input("Buen día, desea una pizza vegetariana? (1)Si (2)No. Digite el número correspondiente: "))
if respuesta == 1:
    ingrediente = int(input("Desea (1)Pimiento o (2)Tofu? Digite el número correspondiente: "))
    if ingrediente == 1:
        print("Su Pizza es Vegetariana con Pimiento, mozzarella y tomate.")
    elif ingrediente == 2:
        print("Su Pizza es Vegetariana con Tofu, mozzarella y tomate.")
    else:
        print("A seleccionado una opción no valida.")
elif respuesta == 2:
    ingrediente = int(input("Desea (1)Peperoni, (2)Jamón o (3)Salmón? Digite el número correspondiente: "))
    if ingrediente == 1:
        print("Su Pizza es No Vegetariana con Peperoni, mozzarella y tomate.")
    elif ingrediente == 2:
        print("Su Pizza es No Vegetariana con Jamón, mozzarella y tomate.")
    elif ingrediente == 3:
        print("Su Pizza es No Vegetariana con Salmón, mozzarella y tomate.")
    else:
        print("A seleccionado una opción no valida.")
else:
    print("A seleccionado una opción no valida.")