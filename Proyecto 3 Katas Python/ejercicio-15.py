# Crea una función lambda que sume 3 a cada 
# número de una lista dada.

# La lista de números
numeros = [1, 2, 3, 4]

# Usamos el map y el lambda y sumamos 3 a cada 
# número
resultado = list(map(lambda x: x + 3, numeros))

print(resultado)