# Genera un programa que nos indique si es de 
# noche, de día o de tarde según la hora 
# proporcionada por el usuario.


# Pido al usuario la hora desde las 00 hasta las 23
hora = int(input("Introduce la hora (00-23): "))


# Determino el momento del día
if 6 <= hora < 12:
    print("Es de día")
elif 12 <= hora < 18:
    print("Es de tarde")
elif 18 <= hora < 24 or 0 <= hora < 6:
    print("Es de noche")
else:
    print("Esa hora no existe")


