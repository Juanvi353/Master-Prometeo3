# Crea una función que tome un nombre completo 
# y una lista de empleados, busque el nombre en 
# la lista y devuelva el puesto del empleado 
# si se encuentra; de lo contrario, devuelve 
# un mensaje indicando que la persona no trabaja 
# aquí.


# Creo la función para buscar al empleado
def buscar_empleado(nombre, empleados):

    # Busco en cada empleado y le devuelo el puesto
    for empleado in empleados:


        if empleado["nombre"] == nombre:
            return empleado["puesto"]
        
    # Si no encuentro a esa persona, 
    # le devuelvo que no trabaja aquí
    return "Esta persona no trabaja aquí"


empleados = [
    {"nombre": "Alba Encinas", "puesto": "Wedding planer"},
    {"nombre": "Juanvi Donas", "puesto": "Programador"},
    {"nombre": "Bartolo Santos", "puesto": "Cajero"},
]


print(buscar_empleado("Alba Encinas", empleados))
print(buscar_empleado("Antonio Flores", empleados))