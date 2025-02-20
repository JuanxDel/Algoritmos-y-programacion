#Entrada
h = int(input("Horas normales trabajadas: "))
pn = int(input("Pago por hora normal: "))
e = int(input("Horas extra trabajadas: "))
nh = int(input("Numero de hijos: "))
#Caja Negra
sb = (h*pn)+(e*pn*1.25)
a1 = 250000
a2 = (173000*nh)
a3 = 180000
d1 = (sb*0.05)
d2 = (sb*0.02)
d3 = (sb*0.07)
dt = (d1+d2+d3)
at = (a1+a2+a3)
sn = (sb+at)-dt
#Salida
print ("Sueldo Base: $", sb)
print ("Actualizacion Academica: $", a1)
print ("Hijos:", nh, "/ Asignacion por hijos: $", a2)
print ("Prima por hogar: $", a3)
print ("Dinero por asignaciones: $", at)
print ("Pago Forzoso: -$", d1)
print ("Pago Habitacional: -$", d2)
print ("Caja de Ahorro: -$", round(d3))
print ("Valor en deducciones: $", dt)
print ("El sueldo neto es: $", sn)

