# Crea una función lambda que filtre los números 
# impares de una lista dada.


numeros = [1, 2, 3, 4, 5, 6, 7]

#Filtro los números impares usando filter y lambda
impares = list(filter(lambda x: x % 2 != 0, numeros))

print(impares)