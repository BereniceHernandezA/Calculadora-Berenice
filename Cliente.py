import xmlrpc.client

# Conexión al Servidor
server = xmlrpc.client.ServerProxy("http://localhost:8000/")

# Menú de opciones y funciones remotas
opciones = {
    1: ("Sumar", server.sumar),
    2: ("Restar", server.restar),
    3: ("Multiplicar", server.multiplicar),
    4: ("Dividir", server.dividir)
}

def menu():
    print("\nCalculadora Remota")
    for key, (nombre, _) in opciones.items():
        print(f"{key}. {nombre}")
    print("5. Salir")
    return int(input("Selecciona una opción: "))

while True:
    opcion = menu()
    if opcion == 5:
        print("\u00a1Adiós! Mi tarea ha sido completada")
        break

    if opcion in opciones:
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))
        nombre, funcion = opciones[opcion]
        print(f"Resultado: {funcion(num1, num2)}")
    else:
        print("Opción no válida. Intenta de nuevo.")
