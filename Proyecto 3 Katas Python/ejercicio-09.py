# Escribe una función que tome una lista de 
# nombres de mascotas como parámetro y devuelva 
# una nueva lista excluyendo ciertas mascotas 
# prohibidas en España. La lista de mascotas 
# a excluir es ["Mapache", "Tigre", "Serpiente 
# Pitón", "Cocodrilo", "Oso"]. Usa la función 
# filter().


# Lista dada en el enunciado
mascotas_prohibidas = ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"]

# Compruebo si está permitida
def mascota_permitida(mascota):
    return mascota not in mascotas_prohibidas

# Filtro la lista de mascotas
def filtrar_mascotas(mascotas):
    # Filter aplica la función mascota_permitida 
    # a cada elemento y list convierte 
    # el resultado en una nueva lista
    return list(filter(mascota_permitida, mascotas))


mascotas = ["Perro", "Gato", "Mapache", "Loro", "Tigre"]
print(filtrar_mascotas(mascotas))