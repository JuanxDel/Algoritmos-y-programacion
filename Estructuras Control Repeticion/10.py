num = int(input("Ingrese un número: "))
suma = sum(i for i in range(1, num) if num % i == 0)

if suma == num:
    print(f"{num} es un número perfecto.")
else:
    print(f"{num} no es un número perfecto.")