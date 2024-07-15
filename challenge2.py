# Este es un Challenge2
print("Challenge2")

Estudiante = "Jon"
Nota1 = 7.0
Nota2 = 5.8
Nota3 = 6.2

NotaFinal = round((7.0 + 5.8 + 6.2)/3,3)
print(f"La nota final de {Estudiante} es {NotaFinal}")

Lab1 = ((7.0)/30)
Lab2 = ((5.8)/50)
Lab3 = ((6.2)/20)

# Diccionario
EstudianteysusNotas = {
    "Nombre" : "Jon",
    "Asignatura" : "Matematicas",
    "Nota1":7.0,
    "Nota2":5.8,
    "Nota3":6.2,
}

Tuplaasig = ("Asignatura")
Tuplalab = ("Nota1", "Nota2", "Nota3")
Tuplafinal = ("Notafinal")

AsignaturaM = list(["Tuplaasig","Tuplalab","Tuplafinal"])

Asignaturaconjunto = set()

print(f"Los datos del estudiante son {EstudianteysusNotas}")
print(f"La nota final de {Estudiante} es {NotaFinal}")
print(f"La {Nota1} vale {Lab1}, {Nota2} vale {Lab2}")