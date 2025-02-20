#Entrada
s = int(input("Ingrese sueldo base: "))
a = int(input("Ingrese venta #1: "))
b = int(input("Ingrese venta #2: "))
c = int(input("Ingrese venta #3: "))
#Caja Negra
sum = (a+b+c)
co = (sum*10)/100
t = (co+sum+s)
#Salida
print ("Dinero obtenido en ventas: ", sum)
print ("Extra por comisiones: ", co)
print ("Dinero total obtenido: ", t)
