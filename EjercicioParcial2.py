'''
Determinar si una palabra ingresada por teclado es un palíndromo. Eliminar espacios y
convertir el texto ingresado a minúsculas. Además, imprimir la palabra invertida. (40 Puntos)
Un palíndromo es una palabra o frase que se lee igual de izquierda a derecha que de derecha a izquierda
Ejemplos:
● Oso
● "Sometamos o matemos"
● "Isaac no ronca así"
● Radar
● Ana
'''
#Añadir primero la palabra
Palabra = input("Ingrese la palabra: ").lower

print(Palabra)

#Luego poner la palabra de forma invertida para saber si es un palídromo o no

print(f"La palabra {Palabra} es un palindromo")


print(f"La palabra {Palabra} no es un palindromo")

