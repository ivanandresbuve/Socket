import socket

soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
soc.bind(('127.0.0.1',9191))
soc.listen()
print('Encendido, Conectando...')

conexion, direccion = soc.accept()
print('Conectado desde: ',direccion)


while True:

    conexion.sendall(b'--Servidor conversor de moneda---\n ***Seleccione la opcion a la que desea convertir la moneda Colombiana***\n 1. Dolar \n 2. Euro \n 3. Peso Mexicano \n 4. Salir')
    p = 3
    while p > 1 or p < 4:
        try :
            recibido = conexion.recv(1024).decode()
            if not recibido:
                break
            rec = str(recibido)
            op = int(rec)
            print("Del cliente recibi: ", recibido)
            if op < 1 or op > 4:
                conexion.sendall(b'Error dato *Ingrese un valor entre 1 a 4')
            else:
                p=10
        except ValueError:
            conexion.sendall(b'Error! Ingrese un dato valido')



    """if recibido.isnumeric():

        op = int(recibido)
        if op < 1 or op > 4:
            conexion.sendall(b'Opcion Invalida!\n *Seleccione una opcion de 1 a 4*\n')

        else:
            if op == 1:
                conexion.sendall(b'Ingresa el valor en pesos Colombianos a convertir a Dolares: ')
                valor = conexion.recv(1024).decode()
                if not valor:
                    break
                elif valor.isnumeric():
                    Dolar = int(valor)
                    if Dolar == 0:
                        conexion.sendall(b'Incorrecto! Ingresa un valor')
                    else:
                        ResultadoDolar = Dolar / 3829.70
                        ResultadoEnviar= str(ResultadoDolar)
                        conexion.sendall(ResultadoEnviar.encode())
                        print(Dolar, 'pesos Colombianos es igual a', ResultadoDolar, 'Dolares')

                else:
                    conexion.sendall(b'Incorrecto! Ingresa un valor')

            elif op == 2:
                conexion.sendall(b'Ingresa el valor en pesos Colombianos a convertir a Euros: ')
                valor = conexion.recv(1024).decode()
                if not valor:
                    break
                elif valor.isnumeric():
                    Euro = int(valor)
                    if Euro == 0:
                        conexion.sendall(b'Incorrecto! Ingresa un valor')
                    else:
                        ResultadoEuro = Euro / 4456.05
                        ResultadoEnviar = str(ResultadoEuro)
                        conexion.sendall(ResultadoEnviar.encode())
                        print(Euro, 'pesos Colombianos es igual a', ResultadoEuro, 'Euros')

                else:
                    conexion.sendall(b'Incorrecto! Ingresa un valor')


            elif op == 3:
                conexion.sendall(b'Ingresa el valor en pesos Colombianos a convertir a Pesos Mexicanos: ')
                valor = conexion.recv(1024).decode()
                if not valor:
                    break
                elif valor.isnumeric():
                    Mex = int(valor)
                    if Mex == 0:
                        conexion.sendall(b'Incorrecto! Ingresa un valor')
                    else:
                        ResultadoMex = Mex / 174.06
                        ResultadoEnviar = str(ResultadoMex)
                        conexion.sendall(ResultadoEnviar.encode())
                        print(Mex, 'pesos Colombianos es igual a', ResultadoMex, 'pesos Mexicanos')

                else:
                    conexion.sendall(b'Incorrecto! Ingresa un valor')

            elif op == 4:
                conexion.sendall(b'Gracias por usar el conversor de monedas')
                print('Conversor de moneda finalizado')
                conexion.close()
                break

    else:
        conexion.sendall(b'Valor incorrecto\n') """