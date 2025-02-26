p=int(input("Ingrese entero P: "))
q=int(input("Ingrese entero Q: "))
r=p**3+q**4-2*p**2
if r>680:
    print("P y Q satisfacen la expresión")
elif r<=680:
    print("P y Q no satisfacen la expresión")