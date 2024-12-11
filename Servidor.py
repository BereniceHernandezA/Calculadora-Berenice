from xmlrpc.server import SimpleXMLRPCServer

# Diccionario de funciones para registrar
funciones = {
    "sumar": lambda a, b: a + b,
    "restar": lambda a, b: a - b,
    "multiplicar": lambda a, b: a * b,
    "dividir": lambda a, b: "Error: División por cero" if b == 0 else a / b
}

# Configurar el servidor
server = SimpleXMLRPCServer(("localhost", 9000))
print("Servidor de calculadora XML-RPC en ejecución...")

# Registrar las funciones
for nombre, funcion in funciones.items():
    server.register_function(funcion, nombre)

# Ejecución del servidor
server.serve_forever()
