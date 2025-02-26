A = int(input("Ingrese el valor de A: "))
B = int(input("Ingrese el valor de B: "))
C = int(input("Ingrese el valor de C: "))
D = int(input("Ingrese el valor de D: "))

N = 1000 * A + 100 * B + 10 * C + D
re = round(N/100)*100

print(f"El número N formado es: ",1000*A + 100*B + 10*C + D)
print(f"El número redondeado a la centena más próxima es: ",re)