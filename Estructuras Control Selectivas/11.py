t=float(input("Digite temperatura: "))
if(t>85):
    print("El deporte adecuado es Natacion")
elif(t>=71 and t<=85):
    print("El deporte adecuado es Tenis")
elif(t>=33 and t<=70):
    print("El deporte adecuado es Golf")
elif(t>=11 and t<=32):
    print("El deporte adecuado es Esquí")
elif(t<=10):
    print("El deporte adecuado es Marcha")
else:
    print("No se identifico deporte")