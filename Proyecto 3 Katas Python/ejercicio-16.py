# Escribe una función que tome una cadena de 
# texto y un número entero n como parámetros y 
# devuelva una lista de todas las palabras 
# que sean más largas que n. 
# Usa la función filter().

# Recibe n y devuelve una función de comprobación
def es_mas_larga_n(n):
    
    def es_mas_larga(palabra):
        # Comprobamos la longitud
        return len(palabra) > n
    return es_mas_larga

# Función que filtra las palabras del texto
def palabras_mas_largas(texto, n):

    palabras = texto.split()


    return list(filter(es_mas_larga_n(n), palabras))

frase = "Hola, mi nombre es Juanvi."
print(palabras_mas_largas(frase, 3))