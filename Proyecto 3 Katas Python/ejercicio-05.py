# Escribe una función que tome una lista
# de números como parámetro y un valor opcional 
# nota_aprobado (por defecto 5). 
# La función debe calcular la media de los números 
# en la lista y determinar si la media es mayor 
# o igual que nota_aprobado. 
# Si es así, el estado será "aprobado"; 
# de lo contrario, "suspenso". 
# La función debe devolver una tupla que contenga 
# la media y el estado.


def calcular_media_y_estado(numeros, nota_aprobado=5):
    # Calculamos la suma de los números
    suma = sum(numeros)

    # Calculamos la cantidad de números en la lista
    cantidad = len(numeros)

    # Calculamos la media diviendo suma entre cantidad
    media = suma / cantidad

    # Comprobamos si la media es amyor o 
    # igual que la nota_aprobado
    if media >= nota_aprobado:
        estado = "aprobado"
    else:
        estado = "suspenso"

    # Devolvemos una tupla con la media y el estado
    return media, estado


notas = [2, 3, 7, 9, 10]
print(calcular_media_y_estado(notas))