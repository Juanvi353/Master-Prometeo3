# Genera una función que convierta una lista 
# de tuplas a una lista de strings. 
# Usa la función map().

# Función que convierte una tupla a un string
def tupla_a_string(tupla):
    return str(tupla)


    # Map aplica la función tupla_a_string a 
    # cada elemento y list convierte el 
    # resultado en una lista
def convertir_tupla_a_string(lista_tuplas):
    return list(map(tupla_a_string, lista_tuplas))


tuplas = [(1, 2),(3, 4),(5, 6)]
print(convertir_tupla_a_string(tuplas))
