interes = 1.04
deposito = float(input(f"Ingrese el monto de positado: "))
print(f"Su Monto al final del Pimer año es: {round(deposito*interes, 2)}")
print(f"Su Monto al final del Segundo año es: {round((deposito*interes)*interes, 2)}")
print(f"Su Monto al final del Tercer año es: {round(((deposito*interes)*interes)*interes, 2)}")
