'''
Escribe un programa que tome una lista de números y devuelva solo los números pares
'''
numeros = [ 1 , 2 , 4 , 5 , 8 , 33 , 82]

for numero in numeros:
    if numero % 2 == 0:
        print(numero)
    