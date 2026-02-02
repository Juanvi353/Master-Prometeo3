# Crea una función que solicite al usuario 
# ingresar una lista de nombres y luego un nombre 
# para buscar en esa lista. Si el nombre está 
# en la lista, imprime un mensaje indicando 
# que fue encontrado; de lo contrario, lanza 
# una excepción.



# Función que pide nombres y busca uno en la lista
def buscar_nombre():
    # Pido los nombres separados por comas
    entrada = input("Introduce una lista de nombres separados por comas: ")

    # Convierto la entrada en una lista y quito espacios
    nombres = [nombre.strip() for nombre in entrada.split(",")]

    # Pido el nombre a buscar
    nombre_buscar = input("Introduce el nombre a buscar: ")

    # Compruebo si el nombre está en la lista
    if nombre_buscar in nombres:
        print("Nombre encontrado.")
    else:
        print("El nombre no se encuentra en la lista.")

buscar_nombre()
