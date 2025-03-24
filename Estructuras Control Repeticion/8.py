total_encuestados = 0
consumen_licor = 0
mujeres_menores = 0
hombres_sin_aguardiente = 0
edad_total_cerveza = 0
consumen_cerveza = 0
consumen_whisky = 0

while True:
    total_encuestados = total_encuestados + 1
    
    consume = input("¿Consume licor? (Sí/No): ")
    if consume == "si":
        consumen_licor = consumen_licor + 1
        licor = int(input("Licor preferido (1-Aguardiente, 2-Ron, 3-Cerveza, 4-Tequila, 5-Whisky, 6-Otro): "))
    elif consume == "no":
        licor = 0
    
    edad = int(input("Ingrese la edad: "))
    sexo = input("Sexo (M/F): ")
    
    if sexo == "F" or "f" and edad < 18:
        mujeres_menores =  mujeres_menores + 1
    
    if sexo == "M" or "m" and 20 <= edad <= 25 and licor != 1:
        hombres_sin_aguardiente = hombres_sin_aguardiente + 1
    
    if licor == 3:
        consumen_cerveza = consumen_cerveza + 1
        edad_total_cerveza = edad_total_cerveza + edad
    
    if licor == 5:
        consumen_whisky = consumen_whisky + 1
    
    continuar = input("¿Desea continuar con la encuesta? (Sí/No): ")
    if continuar != "si":
        break

promedio_cerveza=edad_total_cerveza/consumen_cerveza if consumen_cerveza>0 else 0
porcentaje_whisky = (consumen_whisky / total_encuestados) * 100 

print("Resultados de la encuesta:")
print(f"Total de personas encuestadas que consumen licor: {consumen_licor}")
print(f"Total de mujeres menores de edad: {mujeres_menores}")
print(f"Total de hombres que no consumen aguardiente y tienen entre 20 y 25 años: {hombres_sin_aguardiente}")
print(f"Total de personas encuestadas que consumen licor: {consumen_licor}")
print(f"Promedio de edad de quienes consumen cerveza: {promedio_cerveza}")
print(f"Porcentaje de personas que consumen whisky respecto al total encuestado: {porcentaje_whisky}%")