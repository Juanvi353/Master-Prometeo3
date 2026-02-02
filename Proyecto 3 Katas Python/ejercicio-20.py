# Para una lista con elementos de tipo integer y 
# string, obtén una nueva lista solo con los 
# valores int. Usa la función filter().

# Compruebo si el valor es entero
def es_entero(valor):
    return type(valor) == int


# Filtro solo los enteros de la lista
def filtrar_enteros(lista):
    return list(filter(es_entero, lista))


valores = [1, "hola", 3, "juanvi", 5]
print(filtrar_enteros(valores))
