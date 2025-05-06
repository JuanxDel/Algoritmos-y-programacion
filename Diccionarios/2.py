d = {}
max = 10

print("Introduzca los datos de hasta 10 estudiantes:")

for i in range(1, max + 1):
    print(f"\nEstudiante {i}:")
    nombre = input("Nombre del estudiante (deje vacío para terminar): ")
    if nombre == "":
        break

    nota = float(input("Nota del estudiante (0 a 10): "))

    d[str(i)] = {
        "nombre": nombre,
        "nota": nota
    }

aprobados = []
suspendidos = []
suma_total_notas = 0

for datos in d.values():
    nombre = datos["nombre"]
    nota = datos["nota"]
    suma_total_notas = suma_total_notas + nota
    if nota >= 5:
        aprobados = aprobados + [nombre]
    else:
        suspendidos = suspendidos + [nombre]

cantidad_estudiantes = len(d)
if cantidad_estudiantes > 0:
    nota_media = suma_total_notas / cantidad_estudiantes
else:
    nota_media = 0

print("Estudiantes aprobados:", aprobados)
print("Estudiantes suspendidos:", suspendidos)
print(f"Nota media de la clase: {nota_media:.2f}")