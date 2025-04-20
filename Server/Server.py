import socket

socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_server.bind(('0.0.0.0', 3993))
socket_server.listen()
print("Server is listening on port 3993...")
while True:
    client_socket, addr = socket_server.accept()
    print(f"{addr} has connected to server")
    # client_socket.send(b"Welcome to the server!")