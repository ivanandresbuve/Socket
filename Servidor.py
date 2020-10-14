import socket

soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
soc.bind(('127.0.0.1',9191))
soc.listen()
print('Encendido, Conectando...')

conexion, direccion = soc.accept()
print('Conectado desde: ',direccion)

while True:
    conexion.sendall(b'--Servidor conversor de moneda---\n ***Seleccione la opcion a la que desea convertir la moneda Colombiana***\n 1. Dolar \n 2. Euro \n 3. Peso Mexicano \n 4. Salir')
    p = 0
    while p <= 0 or p >= 5:
        try :
            recibido = conexion.recv(1024).decode()
            if not recibido:
                break
            rec = str(recibido)
            op = int(rec)
            p = op
            print("Del cliente recibi: ", recibido)
            if op < 1 or op > 4:
                conexion.sendall(b'Error dato *Ingrese un valor entre 1 a 4')
        except ValueError:
            conexion.sendall(b'Error! Ingrese un dato valido')

    if op != 4:
        conexion.sendall(b'Ingresa el valor en pesos Colombianos a convertir: ')
        v = 0
        while v <= 0:
            repetir = True
            while repetir == True:
                try:
                    valor = conexion.recv(1024).decode()
                    if not valor:
                        break
                    val = str(valor)
                    valorconv = float(val)
                    v = valorconv
                    repetir = False
                    print("Del cliente recibi: ", valor)
                except ValueError:
                    conexion.sendall(b'Error! Ingrese un dato valido')
            if valorconv <= 0:
                conexion.sendall(b'Error dato! *Ingrese un valor mayor a 0*')

    if op == 1:
        ResultadoDolar = valorconv / 3829.70
        ResultadoEnviar = str(ResultadoDolar)
        conexion.sendall(ResultadoEnviar.encode())
        print(valorconv, 'pesos Colombianos es igual a', ResultadoDolar, 'Dolares')
    elif op == 2:
        ResultadoEuro = valorconv / 4456.05
        ResultadoEnviar = str(ResultadoEuro)
        conexion.sendall(ResultadoEnviar.encode())
        print(valorconv, 'pesos Colombianos es igual a', ResultadoEuro, 'Euros')
    elif op == 3:
        ResultadoMex = valorconv / 174.06
        ResultadoEnviar = str(ResultadoMex)
        conexion.sendall(ResultadoEnviar.encode())
        print(valorconv, 'pesos Colombianos es igual a', ResultadoMex, 'pesos Mexicanos')

    elif op == 4:
        conexion.sendall(b'Gracias por usar el conversor de monedas')
        print('Conversor de moneda finalizado')
        conexion.close()
        break
