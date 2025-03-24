es = int(input("Ingrese el número de estudiantes: "))
max = 0
for i in range(es):
    a = float(input("Ingrese la altura del estudiante: "))
    if a > max:
        max = a
print("La mayor altura es:", max)