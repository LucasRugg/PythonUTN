'''
Escribir un programa que pida al usuario que introduzca una frase en la consola y una vocal, y después muestre por pantalla la misma frase pero con la vocal introducida en mayúscula.
'''

frase = input("Ingrese una frase: ")
vocal = input("Ingrese una vocal: ")
rango = len(frase)
nuevaFrase = ""
for caracter in frase:
    if caracter == vocal:
        nuevaFrase += caracter.upper()
    else:
        nuevaFrase +=caracter
        
print(nuevaFrase)
