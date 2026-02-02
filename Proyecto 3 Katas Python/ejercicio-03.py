# Escribe una función que tome una lista
# de palabras y una palabra objetivo como 
# parámetros. La función debe devolver una lista 
# con todas las palabras de la lista original que 
# contengan la palabra objetivo

def palabras_con_objetivo(lista_palabras, objetivo):
    # Creo una lista vacía donde guardo las
    # palabras que cumplan la condición
    
    resultado = []


    # Recorremos cada palabra de la lista original
    for palabra in lista_palabras:
        # Compruebo si la palabra objetivo está
        # dentro de la palabra actual

        if objetivo in palabra:
            # Si se cumple la condición, añado la palabra
            # a la lista resultado
            resultado.append(palabra)

# Devuelvo la lista con las palabras que contengan
# objetivo

    return resultado

palabras = ["casa", "casar", "casamiento", "python", "buenos dias"]
print(palabras_con_objetivo(palabras, "casa"))

