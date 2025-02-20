#Entrada
h = int(input("NUmero de hombres: "))
m = int(input("Numero de mujeres: "))
#Caja Negra
t = (h+m)
ph = ((h)/t)*100
pm = ((m)/t)*100
#Salida
print ("El porcentaje de hombres es: ", round(ph), "%")
print ("El porcentaje de mujeres es: ", round(pm), "%")
