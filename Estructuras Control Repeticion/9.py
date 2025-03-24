estudiantes = []
puntajes = []
nombres = []

while True:
    nombre = input("Nombre: ")
    puntaje = float(input("Puntaje: "))
    nombres = nombres + [nombre]
    puntajes = puntajes + [puntaje]
    if input("¿Agregar otro? (Si/No): ") != "Si":
        break

if puntajes:
    promedio = sum(puntajes) / len(puntajes)
    max_puntaje = max(puntajes)
    min_puntaje = min(puntajes)
    max_nombre = [nombres[i] for i in range(len(puntajes)) if puntajes[i] == max_puntaje][0]
    min_nombre = [nombres[i] for i in range(len(puntajes)) if puntajes[i] == min_puntaje][0]
    
    print(f"Máximo: {max_nombre}")
    print(f"Mínimo: {min_nombre}")
    print(f"Promedio: {promedio}")
    print(f"% Inferiores: {sum(p < promedio for p in puntajes) * 100 / len(puntajes)}%")
    print(f"% Superiores: {sum(p > promedio for p in puntajes) * 100 / len(puntajes)}%")
else:
    print("No se ingresaron datos.")