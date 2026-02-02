# Escribe un programa en Python que cree 
# una lista de diccionarios con información 
# de estudiantes (nombre, edad, calificación) 
# y use filter para extraer a los estudiantes 
# con una calificación mayor o igual a 90.


estudiantes = [
    {"nombre": "Juanvi", "edad": 22, "calificacion": 9},
     {"nombre": "Alba", "edad": 21, "calificacion": 6.7},
      {"nombre": "Carlos", "edad": 20, "calificacion": 5}
]

# Compruebo si un estudiante tiene mas de un 6
def aprobado(estudiante):
    return estudiante["calificacion"] >= 6

#Uso filter para buscar solo los que tengan mas de un 6
estudiantes_aprobados = list(filter(aprobado, estudiantes))


print(estudiantes_aprobados)