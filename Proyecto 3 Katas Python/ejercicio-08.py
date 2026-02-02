# Escribe un programa que pida al usuario 
# dos números e intente dividirlos. 
# Si el usuario ingresa un valor no numérico o 
# intenta dividir por cero, maneja esas excepciones 
# de manera adecuada y muestra un mensaje 
# indicando si la división fue exitosa o no.

# Pido los dos números en un solo input
num1, num2 = map(float, input("Introduce dos números: ").split())

# Realizo la división
resultado = num1 / num2

# Muestro el resultado
print("Resultado:", resultado)

