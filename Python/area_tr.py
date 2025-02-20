#Entrada
a = float(input("Ingrese el lado A: "))
b = float(input("Ingrese el lado B: "))
c = float(input("Ingrese el lado C: "))
#Caja Negra 
p = (a+b+c)
s = (a+b+c)/2
ar = (s*(s-a)*(s-b)*(s-c))**0.5
#Salida
print ("El perimetro del triangulo es de: ",p)
print ("El semiperimetro del triangulo es de: ",s)
print ("El area total del triangulo es de: ",ar)