producto = input("Ingrese nombre del producto: ")
precio = float(input("Ingrese precio: "))
unidades = int(input("Ingrese número de unidades: "))

costeTotal = precio * unidades

# Formateo de salida usando cadenas de formato
# {:10.2f} indica un número con un total de 10 caracteres (incluyendo el punto decimal y los decimales) y 2 decimales
print("Nombre del producto: {}Precio unitario: {:10.2f} Número de unidades: {:3}Costo total del producto: {:10.2f}".format(producto, precio, unidades, costeTotal))
