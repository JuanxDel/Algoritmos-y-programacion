#Entradas
n=str(input("Ingrese Nombre del Cliente: "))
vc=int(input("Ingrese el Valor de la Compra: "))
#Caja Negra
if vc<50000:
    vp=vc
elif vc>=50000 and vc<100000:
    d=vc*0.05
elif vc>=100000 and vc<700000:
    d=vc*0.11
elif vc>=700000 and vc<1500000:
    d=vc*0.18
elif vc>=1500000:
    d=vc*0.25
vp=vc-d
#Salidas
print ("Nombre del Cliente: ", n)
print ("Valor de la Compra: ", vc)
print ("Valor del Descuento: ", d)
print ("Valor a Pagar: ", vp)