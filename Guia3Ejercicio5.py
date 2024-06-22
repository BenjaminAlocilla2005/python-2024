import random
numero = [random.randint(40, 350) for _ in range(20)]
print("Lista de números generada:")
print(numero)
ni = int(input("Ingrese el número que desea buscar en la lista: ")) #numero a ingresar
nr = numero.count(ni)
print(f"{ni} se repite {nr} veces en la lista.")