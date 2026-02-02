# Calcula la diferencia total en los valores 
# de una lista. Usa la función reduce().


from functools import reduce


# Resto dos valores cualquiera
def restar(a, b):
    return a - b


# Calculo la diferencia total de la lista
def diferencia_total(numeros):

    # Resto los valores de forma acumulativa con reduce
    return reduce(restar, numeros)


print(diferencia_total([2, 5, 8]))