# Genera una función que, para un conjunto de 
# caracteres, devuelva una lista de tuplas 
# con cada letra en mayúsculas y minúsculas. 
# Las letras no pueden estar repetidas. 
# Usa la función map()

# Convierto una letra en una tupla con mayúscula y minúscula
def letra_mayuscula_minuscula(letra):
    return (letra.upper(), letra.lower())

# Recibo el conjunto de caracteres
def convertir_letras(conjunto_caracteres):
    # Elimino las letras repetidas con set
    letras_unicas = set(conjunto_caracteres)

    # El map aplica la función a cada letra 
    # y list lo convierte en lista de tuplas
    return list(map(letra_mayuscula_minuscula, letras_unicas))

caracteres = "Hola"
print(convertir_letras(caracteres))