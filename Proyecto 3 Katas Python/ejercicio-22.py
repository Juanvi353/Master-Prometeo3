# Dada una lista numérica, obtén el producto 
# total de los valores. Usa la función reduce().


from functools import reduce # Sin esto da error en el reduce

# Multiplico los números
def multiplicar(a, b):
    return a * b

# Calculo el producto total de la lista
def producto_total(numeros):


    return reduce(multiplicar, numeros)


print(producto_total([1, 5, 8]))