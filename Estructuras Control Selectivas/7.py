k=int(input("Kilometraje del automovil: "))
if k<300:
    vp=50000
if k>300 and k<1000:
    vr=70000
    e=(k-300)*30000
    vp=vr+e
elif k>1000:
    vr=150000
    e=(k-1000)*9000
    vp=vr+e
print ("El valor a pagar es de: ", vp)