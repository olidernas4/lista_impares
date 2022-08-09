inicio_range = int(input("Ingrese el inicio del rango:"))
fin_range = int(input("Ingrese el final del rango:"))

for numero in range(inicio_range, fin_range+1):
    if numero % 2 != 0:
        print(numero)