i=int(input("Valor de Inversion: "))
t=int(input("Tiempo"))
ie=float(input("Valor de los intereses: "))
c=(i*t*ie)
ct=c+i
if(c>100000):
    print("Debe Reinvertir")
else:
    (c<100000)
    print("No Reinvertir")
print("Los Intereses Obtenidos son: ", c)
print("El capital total obtenido es: ",ct)