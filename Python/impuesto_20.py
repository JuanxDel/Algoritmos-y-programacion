#Entradas
h = int(input("Horas Trabajadas: "))
p = int(input("Pago por Hora: "))
#Caja Negra
s = (h*p)
sn = (s*0.8)
#Salida 
print ("Sueldo base: ", s)
print ("Sueldo neto(descuento impuestos): ", sn)