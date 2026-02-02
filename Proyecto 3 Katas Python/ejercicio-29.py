# Crea una función que convierta una variable 
# en una cadena de texto y enmascare 
# todos los caracteres con el carácter '#' 
# excepto los últimos cuatro.

# En esta función enmascaro una variable 
# dejando visible los últimos 4 caracteres
def enmascarar(valor):
    texto = str(valor)
    return "#" * (len(texto) - 4) + texto[-4:]



print(enmascarar(123456789))
print(enmascarar("abcdefghi"))

