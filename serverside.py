import socket
import threading

clients = []

def handle_client(client_socket, client_address):
    print(f'[Client connected]: {client_address}')
    clients.append(client_socket)
    
    try:
        while True:
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                break
            print(f'[{client_address}]: {message}')
            broadcast_message(message, client_socket)

    except:
        print(f'Client {client_address} disconnected')

    clients.remove(client_socket)
    client_socket.close()
    print(f'Client {client_address} stopped')

def broadcast_message(message, sender_socket):
    for client in clients:
        if client != sender_socket:
            try:
                client.send(str(f"[User 2] {message}").encode('utf-8'))
            except:
                client.close()
                clients.remove(client)

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', 12345))
    server_socket.listen(2)
    print(f'Server is now running on 0.0.0.0:12345')

    while True:
        client_socket, client_address = server_socket.accept()
        client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
        client_thread.start()
    for i in clients:
        i.close()


start_server()
