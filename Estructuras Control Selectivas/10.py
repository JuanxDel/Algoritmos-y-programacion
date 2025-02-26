c=int(input("Ingrese Categoria del trabajador: "))
if c==1:
    sn=5000000
    ns=sn*1.10
elif (c==2):
    sn=4300000
    ns=sn*1.15
elif c==3:
    sn=3600000
    ns=sn*1.2
elif c==4:
    sn=2000000
    ns=sn*1.4
elif c==5:
    sn=900000
    ns=sn*1.6 
#Salida
print("El salario bruto es: ", sn)
print("EL salario bruto mas el aumento es: ", ns)