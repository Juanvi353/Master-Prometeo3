# Escribe una función que reciba una lista 
# de números y calcule su promedio. 
# Si la lista está vacía, lanza una excepción 
# personalizada y maneja el error adecuadamente.


def calcular_promedio(numeros):
        if not numeros:
                return "Error"
        return sum(numeros) / len(numeros)


print(calcular_promedio([4, 6, 8]))
print(calcular_promedio([]))



