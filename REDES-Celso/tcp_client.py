import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

port = 1234
hostname = socket.gethostname()
ip_host = socket.gethostbyname(hostname)



client_socket.connect((ip_host,port))
endereco_cliente, porta_cliente = client_socket.getsockname()
print("Endereco do cliente:", endereco_cliente)
print("Porta do cliente:", porta_cliente)
