n1 = int(input(f"Ingrese un numero: "))
n2 = int(input(f"Ingrese otro numero: "))
print(f"La Suma entre ellos es {n1 + n2}.")
print(f"La Diferencia entre ellos es {n1 - n2}.")
print(f"La Producto entre ellos es {n1 * n2}.")
if (n2 != 0):
    print(f"El Cociente entre ellos es {n1 / n2}.")
else:
    print(f"No se pudo dividir por cero")
print(f"El Promedio entre ellos es {(n1 + n2)/2}.")
print(f"El doble producto del primero menos la mitad del segundo es {2*(n1 + n2/2)}.")