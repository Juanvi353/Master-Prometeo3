# Dada una lista de números, 
# obtén una nueva lista con el doble de cada valor.
# Usa la función map().

def duplicar(x):
    return x * 2
    # Recibe el número y muestra el doble


def duplicar_lista(numeros):
    return list(map(duplicar, numeros))
    # El map aplica la función duplicar a cada elemento y 
    # el list convierte el resultado del map en lista


lista = [1, 2, 3, 4]
print(duplicar_lista(lista))