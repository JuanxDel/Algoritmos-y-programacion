#Entrada
print ("MATEMATICAS")
em = float(input("Ingrese la nota del examen final: "))
tm1 = float(input("Tarea 1: "))
tm2 = float(input("Tarea 2: "))
tm3 = float(input("Tarea 3: "))
print ("FISICA")
ef = float(input("Ingrese la nota del examen final: "))
tf1 = float(input("Tarea 1: "))
tf2 = float(input("Tarea 2: "))
print ("QUIMICA")
eq = float(input("Ingrese la nota del examen final: "))
tq1 = float(input("Tarea 1: "))
tq2 = float(input("Tarea 2: "))
tq3 = float(input("Tarea 3: "))
#Caja Negra
pm0 = (em)*0.9
pm1 = ((tm1+tm2+tm3)/3)*0.1 
pm = (pm0+pm1)
pf0 = (ef)*0.8 
pf1 = ((tf1+tf2)/2)*0.2 
pf = (pf0+pf1)
pq0 = (eq)*0.85
pq1 = ((tq1+tq2+tq3)/3)*0.15
pq = (pq0+pq1)
pt = (pm+pf+pq)/3
#Salida
print ("El promedio en matematicas es: ", round(pm))
print ("El promedio en fisica es: ", round(pf))
print ("El promedio en quimica es: ", round(pq))
print ("El promedio en total de las tres materias es: ", round(pt))