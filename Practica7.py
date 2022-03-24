segundos= int(input(f"Ingrese los Segundos: "))
print(f"{segundos} segundo/s es/1 son {int(segundos//3600)} hora/s, {int((segundos%3600)//60)} minuto/s y {((segundos%3600)%60)} segundo/s")