# 1.Escribe una función que reciba
# una cadena de texto como parámetro
# y devuelva un diccionario con las 
# frecuencias de cada letra en la cadena. 
# Los espacios no deben ser considerados

def frecuencia_letras(texto):
    # He creado el diccionario vacío donde guardo las frecuencias
    frecuencias = {}

    # Recorro cada carácter de la cadena de texto con el for
    for letra in texto:
        # Se comprueba que el carácter sea un espacio
        if letra != " ":
            # Si la letra existe, sumamos 1, y si no, devolvemos 0 y se añade por primera vez
            frecuencias[letra] = frecuencias.get(letra, 0) + 1
    # Devolvemos el diccionario con las frecuencias de cada letra
    return frecuencias

print(frecuencia_letras("hola"))