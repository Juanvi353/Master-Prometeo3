# Escribe una función que calcule el 
# factorial de un número de manera recursiva

def factorial(n):
    # El factorial de 0 o 1 es 1
    if n == 0 or n == 1:
        return 1
    else:
        # Hago la llamada recursiva: 
        # n * factorial del número anterior
        return n * factorial(n - 1)
    
print(factorial(6))
