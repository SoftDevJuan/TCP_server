# TCP_server
Prueba tecnica para crear un cliente y servidor con protocolo TCP usando Python:
Este proyecto implementa un servidor TCP y un cliente TCP en Python que se comunican a través de la misma máquina (`localhost`) utilizando el puerto `5000`. 

## Objetivo

Evaluar conocimientos de redes y programación en Python mediante la creación de un servidor TCP que interactúa con un cliente. El servidor y el cliente están diseñados para recibir y responder mensajes de texto en mayúsculas, así como gestionar solicitudes de desconexión.


## Instrucciones de Ejecución
1. Nececitas tener python instalado y establecido la ruta en el PATH (caso windows)

### 1. Ejecutar el Servidor
1. Asegúrate de estar en el directorio raíz del proyecto (puedes usar powershell).
2. Ejecuta el servidor TCP con el siguiente comando:
   "python server.py"

### 2. Ejecutar el Cliente
1. Asegúrate de estar en el directorio raíz del proyecto (puedes usar powershell).
2. Ejecuta el cliente TCP con el siguiente comando:
   "python cliente.py"


### 4. Envia un mensaje al servidor
1. El cliente te pedira escribir un mensaje para enviar al servidor, escribe tu mensaje y presiona ENTER
2. El servidor respondera con un mensaje igual al tuyo pero en MAYUSCULAS

### 5. Desconexion del server
1. Si deseas terminar tu conexion con el servidor solo tienes que enviar el mensaje con el siguiente texto: "DESCONEXION" (mayusculas)


