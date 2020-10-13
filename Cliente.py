import socket

soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
soc.connect(('127.0.0.1', 9191))
print('Conectado con el servidor')

while True:
    datos = soc.recv(1024).decode()
    if not datos:
        break
    print('Mensaje del servidor: ', datos)

    #Enviar informacion
    enviar = str(input())
    soc.sendall(enviar.encode())

