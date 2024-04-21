'''
Escribe un programa que tome una lista de números y calcule la suma de todos los
elementos.
'''

numeros = [4 , 6 , 11 , 22 , 30]
suma = 0

for numero in numeros:
    suma = suma + numero
    
print("La suma de todos los elementos de la lista es: " , suma)