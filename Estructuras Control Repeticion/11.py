saldo = 1000
while True:
    print("1. Depositar dinero")
    print("2. Retirar dinero")
    print("3. Consultar saldo")
    print("4. Salir")

    opcion = input("Seleccione una opción: ")
    
    if opcion == "1":
        monto = float(input("Ingrese el monto a depositar: "))
        if monto > 0:
            saldo = saldo + monto
            print(f"Nuevo saldo: {saldo}")
        else:
            print("Monto inválido.")
    
    elif opcion == "2":
        monto = float(input("Ingrese el monto a retirar: "))
        if 0 < monto <= saldo:
            saldo = saldo - monto
            print(f"Nuevo saldo: {saldo}")
        else:
            print("Saldo insuficiente o monto inválido.")
    
    elif opcion == "3":
        print(f"Saldo actual: {saldo}")
    
    elif opcion == "4":
        print("Gracias por usar el cajero automático.")
        break
    
    else:
        print("Opción inválida, intente nuevamente.")
