# Escribe un programa en Python que utilice condicionales para determinar el monto final de una compra en una tienda en línea, después de aplicar un descuento. El programa debe:
# a. Solicitar al usuario el precio original de un artículo.
# b. Preguntar si tiene un cupón de descuento (respuesta sí o no).
# c. Si la respuesta es sí, solicitar el valor del cupón de descuento.
# d. Aplicar el descuento al precio original, siempre que el valor del cupón sea válido (mayor a cero).
# e. Mostrar el precio final de la compra, considerando o no el descuento.
# f. Usar estructuras de control de flujo (if, elif, else) para llevar a cabo las acciones.


# Pido al usuario el precio original
precio_original = float(input("Introduce el precio original: "))


#  Pregunto si tiene un cupón de descuento
tiene_cupon = input("¿Tienes un cupón de descuento?")


# Inicializo el precio final como el precio original
precio_final = precio_original


# Si tiene cupón, aplicamos el descuento si es válido
if tiene_cupon == "si":
    cupon = float(input("Introduce el valor del cupón: "))
    if cupon > 0:
        precio_final -= cupon
        if precio_final < 0: # El precio no puede ser negativo
            precio_final = 0
    
    else:
        print("Valor del cupón no válido. No hay descuento")

elif tiene_cupon == "no":
    pass # No hay descuento

else:
    print("Respuesta no válida")


# Muestro el precio final
print(f"El precio final de la compra es: {precio_final}")
