# Escribe un programa que pida al usuario 
# que introduzca su edad. Si el usuario ingresa 
# un valor no numérico o un valor fuera del rango 
# esperado (por ejemplo, menor que 0 o mayor 
# que 120), maneja las excepciones adecuadamente


edad = input("Introduce tu edad: ")

# Compruebo que el valor es numérico
if not edad.isdigit():
    print("Error: debes introducir un número.")
else:
    edad = int(edad)

    # Compruebo que la edad esté en el rango válido
    if edad < 0 or edad > 120:
        print("Error: la edad debe estar entre 0 y 120.")
    else:
        print("Edad introducida correctamente:", edad)