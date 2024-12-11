import xmlrpc.client

# Coneccion al Servidor
server = xmlrpc.client.ServerProxy("http://localhost:8000/")

# Menú de la calculadora
def menu():
    print("\nCalculadora Remota")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")
    return int(input("Selecciona una opción: "))

while True:
    opcion = menu()
    if opcion == 5:
        print("¡Adiós! Mi tarea a sido completada")
        break

    num1 = float(input("Ingresa el primer número: "))
    num2 = float(input("Ingresa el segundo número: "))

    if opcion == 1:
        print(f"Resultado: {server.sumar(num1, num2)}")
    elif opcion == 2:
        print(f"Resultado: {server.restar(num1, num2)}")
    elif opcion == 3:
        print(f"Resultado: {server.multiplicar(num1, num2)}")
    elif opcion == 4:
        print(f"Resultado: {server.dividir(num1, num2)}")
    else:
        print("Opción no válida. Intenta de nuevo.")
