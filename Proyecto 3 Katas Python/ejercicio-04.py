# Genera una función que calcule la diferencia 
# entre los valores de dos listas. 
# Usa la función map()


# Función que calcula la diferencia
def restar(x, y):
    return x - y

# Función que calcula la diferencia 
# entre los valores de dos listas
def diferencia_listas(lista1, lista2):

    # El map aplica la función de restar a 
    # los elementos de ambas listas
    return list(map(restar, lista1, lista2))

l1 = [10, 20, 30]
l2 = [2, 4, 6]
print(diferencia_listas(l1, l2))