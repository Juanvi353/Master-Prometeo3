# Escribe un programa que determine qué calificación en texto tiene un alumno según su calificación numérica.
# Reglas:
# 0 - 69: insuficiente
# 70 - 79: bien
# 80 - 89: muy bien
# 90 - 100: excelente


# Pido la calificación del alumno
calificacion = int(input("Introduce la calificacion: "))


# Determino la calificación en texto
if 0 <= calificacion <= 69:
    print("Insuficiente")
elif 70 <= calificacion <= 79:
    print("Bien")
elif 80 <= calificacion <= 89:
    print("Muy bien")
elif 90 <= calificacion <= 100:
    print("Excelente")
else:
    print("Esa calificacion no es válida")


