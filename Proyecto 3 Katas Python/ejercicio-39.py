# Escribe una función que tome dos parámetros: 
# figura (una cadena que puede ser "rectangulo", 
# "circulo" o "triangulo") y datos (una tupla con 
# los datos necesarios para calcular el área de 
# la figura).


import math # Es necesario para poder calcular el área


# Función que calcula el área según la figura
def calcular_area(figura, datos):
    if figura == "rectangulo":
        base, altura = datos
        return base * altura

    elif figura == "circulo":
        radio, = datos
        return math.pi * radio ** 2
    
    elif figura == "triangulo":
        base, altura = datos
        return (base * altura) / 2
    else:
        return "La figura no es válida"
    


print(calcular_area("rectangulo", (6, 4)))
print(calcular_area("circulo", (5,)))
print(calcular_area("triangulo", (6, 3)))