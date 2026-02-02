# Crea una función que determine si dos palabras 
# son anagramas, es decir, si están formadas 
# por las mismas letras pero en diferente orden.


def son_anagramas(palabra1, palabra2):

    # Ordeno las letras de cada palabra y comparo
    return sorted(palabra1) == sorted(palabra2)



print(son_anagramas("amor", "roma"))
print(son_anagramas("hola", "juanvi"))