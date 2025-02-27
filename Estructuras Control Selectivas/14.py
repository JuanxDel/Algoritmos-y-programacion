a=float(input("Ingrese lectura anterior: "))
b=float(input("Ingrese lecrura actual: "))
if a>b:
    l=a-b
elif a<b:
    l=b-a
if l>=0 and l<=100:
    vp=1004.600*l
elif l>100 and l<=300:
    vp=30080.00*l
elif l>300 and l<=500:
    vp=500100.000*l
elif l>500:
    vp=120.000*l
print("El valor a pagar es de: ", vp)