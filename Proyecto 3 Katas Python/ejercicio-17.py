#Crea una función que tome una lista de dígitos 
# y devuelva el número correspondiente. 
# Por ejemplo, [5,7,2] corresponde al número 572. 
# Usa la función reduce().

import functools

# Combino los digitos en un número
def unir_digitos(acumulado, digito):
    return acumulado * 10 + digito

# Convierto la lista de digitos en número con reduce
def lista_a_numero(digitos):
    return functools.reduce(unir_digitos, digitos)


print(lista_a_numero([5, 7, 2]))

# He tenido que buscar información del functools 
# porque no me dejaba usar el reduce 
# solo de por si
