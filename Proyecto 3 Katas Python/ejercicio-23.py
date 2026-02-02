# Concatena una lista de palabras. 
# Usa la función reduce().


from functools import reduce


# Concateno dos palabras cualquiera
def concatenar(a, b):
    return a + b


# Concateno la lista de palabras
def concatenar_palabras(palabras):

    # Uno todas en una sola con reduce
    return reduce(concatenar, palabras)


print(concatenar_palabras(["Hola", " ", "soy", " ", "Juanvi"]))
