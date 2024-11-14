# crear un cliente que se conecte al server TCP via localhost a traves del puerto 5000
# el cliente solicitar al usuario escribir un mensaje para enviar al servidor
# el cliente debe recibir el mensaje del servidor y mostrarlo
# para desconectarse del servidor se debe escribir "DESCONEXION" em mayusculas

import socket
direccion_server = ('localhost', 5000)
socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_cliente.connect(direccion_server)
print(f"se establecio conexion con el server: {direccion_server}")

try:
    while True:
        mensaje = input("Escribe un mensaje para enviar: ")
        socket_cliente.sendall(mensaje.encode())
        if mensaje == "DESCONEXION":
            break

        datos_servidor = socket_cliente.recv(1024)
        print(f"servidor dice: {datos_servidor.decode()}")
finally:
    socket_cliente.close()
    print("se cerro la conexion con el servidor")


