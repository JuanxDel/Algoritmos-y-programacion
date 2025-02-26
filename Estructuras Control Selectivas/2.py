s=int(input("Ingrese valor de el salario"))
if s<900000:
    sn=(s*1.15)
    print(round(sn))
elif s>=900000:
    sn=(s*1.12)
    print(round(sn))
