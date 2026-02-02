# Crea una función que retorne las palabras 
# de una lista que comiencen con una letra
# en específico. Usa la función filter().

# Compruebo si una palabra empieza por una letra concreta
def empieza_por_letra(letra):
    def empieza(palabra):
        return palabra.startswith(letra)
    return empieza

# Filtramos las palabras
def filtrar_por_letra(lista_palabras, letra):
    return list(filter(empieza_por_letra(letra), lista_palabras))


palabras = ["perro", "pez", "puercoespin", "tigre", "serpiente", "armadillo"]
print(filtrar_por_letra(palabras, "p"))