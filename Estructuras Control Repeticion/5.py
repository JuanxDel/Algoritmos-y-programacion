s = 0
k = 1
while s <= 1000:
    s=s+(k**2+1)/k
    k=k+1
print ("La cantidad de terminos necesarios fue:", k-1)