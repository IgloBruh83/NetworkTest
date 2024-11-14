import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('0.0.0.0', 22222))
server_socket.listen(1)

print("Server started...")

while True:
    client_socket, addr = server_socket.accept()
    print(f"{addr} is now connected")

    data = client_socket.recv(1024).decode('utf-8')
    print(f"[Client {addr}]: {data}")

    response = "Response text"
    client_socket.send(response.encode('utf-8'))

    client_socket.close()
