# Script Python for Test of concepts about network
# Autor: Mateus Pantoja

# Subject: Computer Networks

import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

port = 1234
hostname = socket.gethostname()
ip_host = socket.gethostbyname(hostname)

print("Server - Hostname: {}".format(hostname))
print("Server - IP: {}".format(ip_host))


server_socket.bind((ip_host, port))

server_socket.listen()


while True:
    client_socket, client_addr = server_socket.accept()
    # print(type(client_socket))
    print(client_socket)
    print(type(client_addr))
    print(client_addr)

    print("Connected to {}\n".format(client_addr))

