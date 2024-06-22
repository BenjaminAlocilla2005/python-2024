'''
1. Obtener la cantidad de veces que se repite la palabra “universidad” dentro del siguiente
parrafo: ´
“La Universidad de los Lagos es una institucion estatal fundada en 1993. Esta universidad regional 
entrega una contribucion significativa al desarrollo sostenible del territorio. Como Universidad sus 
pilares fundamentales se basan en la inclusion, pluralismo, conciencia ambiental y participacion
democratica.” ´
Guardar las palabras encontradas dentro de una tupla.
'''
p = "La Universidad de los Lagos es una institucion estatal funadada en 1993. Esta universidad regional entrega una contribucion significativa al desarrollo sostenible del territorio. Como Universidad sus pilares fundamentales se basan en la inclusion, pluralismo, conciencia ambiental y participacion democratica"

minus = p.lower() #Se deja todo en minusculas para poder contar todas las palabras.

r = minus.count("universidad")

cp = ("universidad") * r 

print(f"La palabra universidad se repite {r} veces.")

print(f"Las palabras guardadas en la tupla:",cp)