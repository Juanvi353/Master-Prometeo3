# Crea una función que busque y devuelva el 
# primer elemento duplicado en una lista dada.


# Devuelvo el primer elemento duplicado de una lista
def primer_duplicado(lista):
    vistos = set() # Guardo los elementos vistos con set()


    for elemento in lista:
        if elemento in vistos: # Si lo hemos visto, pasa a duplicados
            return elemento
        vistos.add(elemento)


    return None # Si no hay duplicados, soltamos None


print(primer_duplicado([4, 6, 7, 3]))
print(primer_duplicado([2, 1, 2, 3, 4, 9]))


