# Crea la clase UsuarioBanco
# Representa a un usuario de un banco con su nombre, saldo y si tiene o no cuenta corriente.
# Métodos: retirar_dinero, transferir_dinero, agregar_dinero.
# Código a seguir:
# Inicializar un usuario con nombre, saldo y un indicador (True o False) de cuenta corriente.
# Implementar retirar_dinero para sustraer dinero del saldo, lanzando un error si no es posible.
# Implementar transferir_dinero para transferir dinero desde otro usuario, lanzando un error en caso de fallo.
# Implementar agregar_dinero para aumentar el saldo del usuario.
# Caso de uso:
# a. Crear dos usuarios: "Alicia" con saldo inicial de 100 y "Bob" con saldo inicial de 50, ambos con cuenta corriente.
# b. Agregar 20 unidades al saldo de Bob.
# c. Transferir 80 unidades de Bob a Alicia.
# d. Retirar 50 unidades del saldo de Alicia.


# Defino la clase UsuarioBanco
class UsuarioBanco:
    def __init__(self, nombre, saldo, cuenta_corriente):
        self.nombre = nombre
        self.saldo = saldo
        self.cuenta_corriente = cuenta_corriente


    # Método para retirar dinero
    def retirar_dinero(self, cantidad):
        if cantidad <= 0:
            raise ValueError("La cantidad a retirar no puede ser menor que 0 ó 0!")
        if cantidad > self.saldo:
            raise ValueError(f"{self.nombre} no tiene suficiente saldo para retirar")
        self.saldo -= cantidad


    # Método para tranferir dinero a otro usuario
    def transferir_dinero(self, otro_usuario, cantidad):
        if cantidad <= 0:
            raise ValueError("La cantidad a transferir no puede ser menor que 0 ó 0!")
        if cantidad > otro_usuario.saldo:
            raise ValueError(f"{otro_usuario.nombre} no tiene suficiente dinero para realizar la transferencia")
        
        # Resto al usuario que lo transfiere
        otro_usuario.saldo -= cantidad

        # Sumo al usuario que lo recibe
        self.saldo += cantidad


    # Método para añadir dinero
    def agregar_dinero(self, cantidad):
        if cantidad <= 0:
            raise ValueError ("La cantidad a añadir no puede ser menor o igual que 0!")
        self.saldo += cantidad


# Creo dos usuarios
alicia = UsuarioBanco("Alicia", 100, True)
bob = UsuarioBanco("Bob", 50, True)

# Añado 20 euros a Bob
bob.agregar_dinero(20)

# Transfiero 80 euros de Bob a Alicia
alicia.transferir_dinero(bob, 70)

# Retiro 50 euros del saldo de Alicia
alicia.retirar_dinero(50)



print(f"Saldo Alicia: {alicia.saldo}")
print(f"Saldo Bob: {bob.saldo}")