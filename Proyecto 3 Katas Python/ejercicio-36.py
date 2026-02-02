# Crea una función llamada procesar_texto
# Procesa un texto según la opción especificada: contar_palabras, reemplazar_palabras o eliminar_palabra.
# Código a seguir:
# Crear una función contar_palabras que cuente el número de veces que aparece cada palabra en el texto y devuelva un diccionario.
# Crear una función reemplazar_palabras para sustituir una palabra_original por una palabra_nueva en el texto y devolver el texto modificado.
# Crear una función eliminar_palabra que elimine una palabra del texto y devuelva el texto sin ella.
# Crear la función procesar_texto que reciba un texto, una opción ("contar", "reemplazar", "eliminar") y un número variable de argumentos según la opción elegida.
# Caso de uso:
# Verificar el funcionamiento completo de procesar_texto.


# Cuenta las veces que aparece cada palabra
def contar_palabras(texto):
    palabras = texto.split() # Separamos el texto
    conteo = {} # Diccionario vacío

    for palabra in palabras:
        conteo[palabra] = conteo.get(palabra, 0) + 1
    return conteo


# Reemplaza una palabra por otra
def reemplazar_palabras(texto, palabra_original, palabra_nueva):
    return texto.replace(palabra_original, palabra_nueva)


# Elimina una palabra del texto
def eliminar_palabra(texto, palabra):
    palabras = texto.split()
    palabras = [p for p in palabras if p != palabra]
    return " ".join(palabras)


# Procesa el texto según la opción elegida 
def procesar_texto(texto, opcion, *args):
    if opcion == "contar":
        return contar_palabras(texto)
    elif opcion == "reemplazar":
        return reemplazar_palabras(texto, args[0], args[1])
    elif opcion == "eliminar":
        return eliminar_palabra(texto, args[0])
    else:
        return "Opción no válida"
    




texto = "Hola, me llamo Juanvi"

print(procesar_texto(texto, "contar"))
print(procesar_texto(texto, "reemplazar", "hola", "adios"))
print(procesar_texto(texto, "eliminar", "hola"))