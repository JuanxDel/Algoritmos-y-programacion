#Entrada
na = int(input("Primera nota parcial: "))
nb = int(input("Segunda nota parcial: "))
nc = int(input("Tercera nota parcial: "))
ef = int(input("Calificacion Examen: "))
tf = int(input("Calificacion Trabajo: "))
#Caja Negra
p1 = ((na+nb+nc)/3)*0.55
p2 = (ef)*0.3
p3 = (tf)*0.15
nf = (p1+p2+p3)
#Salida
print ("La nota final es de: ", nf)
