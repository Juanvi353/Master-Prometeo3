# Crea la clase Arbol
# Define un árbol genérico con un tronco y ramas como atributos.
# Métodos disponibles: crecer_tronco, nueva_rama, crecer_ramas, quitar_rama, info_arbol.
# Código a seguir:
# Inicializar un árbol con un tronco de longitud 1 y una lista vacía de ramas.
# Implementar el método crecer_tronco para aumentar la longitud del tronco en una unidad.
# Implementar el método nueva_rama para agregar una nueva rama de longitud 1 a la lista de ramas.
# Implementar el método crecer_ramas para aumentar en una unidad la longitud de todas las ramas existentes.
# Implementar el método quitar_rama para eliminar una rama en una posición específica.
# Implementar el método info_arbol para devolver información sobre la longitud del tronco, el número de ramas y sus longitudes.
# Caso de uso:
# a. Crear un árbol.
# b. Hacer crecer el tronco una unidad.
# c. Añadir una nueva rama.
# d. Hacer crecer todas las ramas una unidad.
# e. Añadir dos nuevas ramas.
# f. Retirar la rama situada en la posición 2.
# g. Obtener información sobre el árbol.


# Defino la clase Arbol
class Arbol:
    def __init__(self):
        self.tronco = 1        # Longitud inicial del tronco
        self.ramas = []        # Lista vacía de ramas

    # Método para hacer crecer el tronco
    def crecer_tronco(self):
        self.tronco += 1

    # Método para añadir una nueva rama
    def nueva_rama(self):
        self.ramas.append(1)

    # Método para hacer crecer todas las ramas
    def crecer_ramas(self):
        self.ramas = [rama + 1 for rama in self.ramas]

    # Método para quitar una rama por posición
    def quitar_rama(self, posicion):
        if 0 <= posicion < len(self.ramas):
            self.ramas.pop(posicion)

    # Método para mostrar información del árbol
    def info_arbol(self):
        return {
            "longitud_tronco": self.tronco,
            "numero_ramas": len(self.ramas),
            "longitudes_ramas": self.ramas
        }
    


arbol = Arbol()

arbol.crecer_tronco()

arbol.nueva_rama()

arbol.crecer_ramas()

arbol.nueva_rama()

arbol.nueva_rama()

arbol.quitar_rama(2)

print(arbol.info_arbol())