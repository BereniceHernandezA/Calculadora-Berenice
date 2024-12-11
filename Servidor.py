from xmlrpc.server import SimpleXMLRPCServer

# Funciones 
def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Error: División por cero"
    return a / b


server = SimpleXMLRPCServer(("localhost", 9000))
print("Servidor de calculadora XML-RPC en ejecución...")

# Registrar las funciones
server.register_function(sumar, "sumar")
server.register_function(restar, "restar")
server.register_function(multiplicar, "multiplicar")
server.register_function(dividir, "dividir")

# Ejecucion del Servidor
server.serve_forever()
