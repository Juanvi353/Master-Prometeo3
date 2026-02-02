# Genera una función que, al recibir una frase, 
# devuelva una lista con la longitud de 
# cada palabra. Usa la función map()

# Devuelvo la longitud de la palabra
def longitud_palabra(palabra):
    return len(palabra)

# Recibe la frase y devuelve la lista con la longitud
def longitudes_palabras(frase):

    # Separo la frase en palabras usando los espacios
    palabras = frase.split()

    # El map aplica la función longitud_palabra 
    # a cada palabra y list lo convierte en lista
    return list(map(longitud_palabra, palabras))


frase = "Hola, mi nombre en Juanvi"
print(longitudes_palabras(frase))