usuarios = {
    "iperurena": {
        "nombre": "Iñaki",
        "apellido": "Perurena",
        "c": "123123"
    },
    "fmuguruza": {
        "nombre": "Fermín",
        "apellido": "Muguruza",
        "c": "654321"
    },
    "aolaizola": {
        "nombre": "Aimar",
        "apellido": "Olaizola",
        "c": "123456"
    }
}

intentos = 0
max_intentos = 3

while intentos < max_intentos:
    usuario = input("Ingrese su usuario: ")
    c = input("Ingrese su contraseña: ")

    if usuario in usuarios and usuarios[usuario]["c"] == c:
        print(f"Bienvenido, {usuarios[usuario]['nombre']} {usuarios[usuario]['apellido']}")
        break
    else:
        intentos = intentos + 1
        if intentos < max_intentos:
            print(f"Intento incorrecto. Te quedan {max_intentos - intentos} intentos.")
        else:
            print("Has superado el número máximo de intentos.")