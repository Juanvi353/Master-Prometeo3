# Crea una función lambda que sume 
# elementos correspondientes de dos listas dadas.



lista1 = [1, 2, 3]
lista2 = [4, 5, 6]


suma_listas = list(map(lambda x, y: x + y, lista1, lista2))


print(suma_listas)