import socket

soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
soc.bind(('127.0.0.1', 9191))
soc.listen()
print('Encendido, Conectando...')

conexion, direccion = soc.accept()
print('Conectado desde: ', direccion)

while True:
    conexion.sendall(b'--Servidor conversor de moneda---'
                     b'\n\n**Seleccione la opcion a la que desea convertir la moneda Colombiana**'
                     b'\n 1. Dolar \n 2. Euro \n 3. Peso Mexicano \n 4. Salir')

    p = 0
    while p <= 0 or p >= 5:
        try:
            recibido = conexion.recv(1024).decode()
            op = int(recibido)
            p = op
            print("Del cliente recibi: ", recibido)
            if op < 1 or op > 4 or not recibido:
                conexion.sendall(b'La opcion no es valida! *Por favor ingrese una opcion de 1 a 4*')
        except ValueError:
            conexion.sendall(b'No ingreso un numero! *Por favor ingrese una opcion de 1 a 4*')

    if op != 4:
        conexion.sendall(b'Ingresa el valor en pesos Colombianos a convertir: ')
        v = 0
        while v <= 0:
            try:
                valor = conexion.recv(1024).decode()
                valorconv = float(valor)
                v = valorconv
                print("Del cliente recibi: ", valor)
                if valorconv <= 0 or not valor:
                    conexion.sendall(b'El numero ingresado es negativo o cero! *Ingrese un valor mayor a 0*')
            except ValueError:
                conexion.sendall(b'No ha ingresado un numero! *Por favor ingrese un valor mayor a 0*')

    if op == 1:
        ResultadoDolar = valorconv / 3829.70
        conexion.sendall((str(valorconv) + ' pesos Colombianos son ' + str(ResultadoDolar) + ' Dolares'
                          + '\n*Presiones Enter para continuar*').encode())
        print(valorconv, 'pesos Colombianos es igual a', ResultadoDolar, 'Dolares')

    elif op == 2:
        ResultadoEuro = valorconv / 4456.05
        conexion.sendall((str(valorconv) + ' pesos Colombianos es igual a ' + str(ResultadoEuro) + ' Euros'
                          + '\n*Presiones Enter para continuar*').encode())
        print(valorconv, 'pesos Colombianos es igual a', ResultadoEuro, 'Euros')

    elif op == 3:
        ResultadoMex = valorconv / 174.06
        conexion.sendall((str(valorconv) + ' pesos Colombianos son ' + str(ResultadoMex) + ' pesos Mexicanos'
                          + '\n*Presiones Enter para continuar*').encode())
        print(valorconv, 'pesos Colombianos es igual a', ResultadoMex, 'pesos Mexicanos')

    elif op == 4:
        conexion.sendall(b'Gracias por usar el conversor de monedas \n *Presiona Enter para salir*')
        print('Conversor de moneda finalizado')
        conexion.close()
        break
