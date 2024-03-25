producto = input("Ingrese nombre del producto: ")
precio = float(input("Ingrese precio: "))
unidades = int(input("Ingrese número de unidades: "))

costeTotal = precio * unidades

# Formateo de salida usando cadenas de formato
# {:10.2f} indica un número con un total de 10 caracteres (incluyendo el punto decimal y los decimales) y 2 decimales
print("\nNombre del producto: {}\nPrecio unitario: {:10.2f}\nNúmero de unidades: {:3}\nCosto total del producto: {:10.2f}".format(producto.upper(), precio, unidades, costeTotal))
