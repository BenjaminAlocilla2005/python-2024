'''
Se cuenta con tres tuplas: la primera contiene los puntajes más altos obtenidos por
estudiantes en Matemáticas. La segunda tupla contiene los puntajes más altos en Química.
Por último, la tercera tupla contiene los puntajes más altos en Programación.
● Puntajes Matemáticas = (55, 17, 93, 75, 88, 55)
● Puntajes Química = (10, 85, 75, 88, 91, 75)
● Puntajes Programación = (68, 78, 85, 68, 82, 10)
A) Imprimir los valores duplicados de cada tupla
B) Convertir cada tupla en una lista y ordenar las listas en orden descendente.
C) Unir las listas anteriormente generadas en una sola y eliminar los duplicados.
D) Encontrar el puntaje máximo y mínimo de la lista resultante.
'''
# Tuplas
Matemáticas = (55,17,93,75,88,55)
Química = (10,85,75,88,91,75)
Programación = (68,78,85,68,82,10)

Materias = ('Mate','Química','Progra')
Puntuacion = (Matemáticas, Química, Programación)

for i in range(len(Materias)):
    Asignaturas = Materias[i] #Nombre actual del ramo
    Puntajes = Puntuacion[i] #Puntaje actual del ramo

    temp = set() #Conjunto Temporal para guardar valores unicos
    duplicados = [] #Lista vacia donde guarda duplicados

    for j in Puntajes:
        if j in temp:
            duplicados.append(j)
        else:
            temp.add(j)

        if duplicados:
            print()
    print(duplicados)

    for Asignaturas in Materias:
        if Materias.count(Asignaturas) > 1 and Asignaturas not in duplicados:
            duplicados.append(Asignaturas)

    print(f"Valores duplicados en {Asignaturas}: {tuple(duplicados)}")

Notas = 55 in Matemáticas and 75 in Química and 68 in Programación
print(Notas)

# C)Unir las tuplas en una sola y eliminar los duplicados
newtupla = tuple(set(Matemáticas + Química + Programación))
print(f"Tupla unida sin duplicados: {newtupla}")

# D)Transformar la tupla obtenida en una lista. Imprimir la nueva lista obtenida
newlista = list(newtupla)
print(f"Lista de notas: {newlista}")