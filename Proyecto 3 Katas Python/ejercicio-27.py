# Crea una función que calcule el promedio de una 
# lista de números.


# Se calcula el promedio con esta función
def calcular_promedio(numeros):

    # Sumo todos los valores
    suma = sum(numeros)


    # Divido entre la cantidad de números
    return suma / len(numeros)

print(calcular_promedio([3, 4, 7]))