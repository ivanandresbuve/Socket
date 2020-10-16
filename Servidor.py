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
    op = 4
    while p <= 0 or p >= 5:
        try:
            op = int(conexion.recv(1024).decode())
            p = op
            print("Del cliente recibi: ", op)
            if op < 1 or op > 4 or not op:
                conexion.sendall(b'La opcion no es valida! *Por favor ingrese una opcion de 1 a 4*')
        except ValueError:
            conexion.sendall(b'No ingreso un numero! *Por favor ingrese una opcion de 1 a 4*')

    valor = 0
    if op != 4:
        conexion.sendall(b'Ingresa el valor en pesos Colombianos a convertir: ')
        while valor <= 0:
            try:
                valor = float(conexion.recv(1024).decode())
                print("Del cliente recibi: ", valor)
                if valor <= 0 or not valor:
                    conexion.sendall(b'El numero ingresado es negativo o cero! *Ingrese un valor mayor a 0*')
            except ValueError:
                conexion.sendall(b'No ha ingresado un numero! *Por favor ingrese un valor mayor a 0*')

    if op == 1:
        ResultadoDolar = valor / 3829.70
        conexion.sendall((str(valor) + ' pesos Colombianos son ' + str(ResultadoDolar) + ' Dolares'
                          + '\n*Presiones Enter para continuar*').encode())
        print(valor, 'pesos Colombianos es igual a', ResultadoDolar, 'Dolares')

    elif op == 2:
        ResultadoEuro = valor / 4456.05
        conexion.sendall((str(valor) + ' pesos Colombianos es igual a ' + str(ResultadoEuro) + ' Euros'
                          + '\n*Presiones Enter para continuar*').encode())
        print(valor, 'pesos Colombianos es igual a', ResultadoEuro, 'Euros')

    elif op == 3:
        ResultadoMex = valor / 174.06
        conexion.sendall((str(valor) + ' pesos Colombianos son ' + str(ResultadoMex) + ' pesos Mexicanos'
                          + '\n*Presiones Enter para continuar*').encode())
        print(valor, 'pesos Colombianos es igual a', ResultadoMex, 'pesos Mexicanos')

    elif op == 4:
        conexion.sendall(b'Gracias por usar el conversor de monedas \n *Presiona Enter para salir*')
        print('Conversor de moneda finalizado')
        conexion.close()
        break
