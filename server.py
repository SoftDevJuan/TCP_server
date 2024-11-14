# crear un servidor TCP que utilice el puerto 5000 en local
# el servidor debe escuchar en el puerto 5000 por conexiones nuevas
# el servidor debe recibir los mensajes del cliente y regresarlos en MAYUSCULA
# si recibe el texto "DESCONEXION" en mayusculas debe terminar la conexion con el cliente
# se debe mantener en linea para nuevas conexiones

import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_add = ('localhost', 5000)
server_socket.bind(server_add)
server_socket.listen()
print(f"servidor escuchando en {server_add}")
while True:
    conn, cliente = server_socket.accept()
    try:
        print(f"conexion establecida con {cliente}")
        while True:
            data = conn.recv(1024)
            mensaje_recibido = data.decode()
            if mensaje_recibido == "DESCONEXION":
                print("conexion cerrada por el cliente")
                break
            else:
                print(f"recibido: {data.decode()}")
                conn.sendall(data.upper())     
    finally:
        conn.close()

