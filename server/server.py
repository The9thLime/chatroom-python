import socket
import threading

clients = []

def handle_client(client_socket, client_address):
    while True:
        try:
            message = client_socket.recv(1024)
            if message:
                broadcast_message = f"[{client_address[0]}:{client_address[1]}] ".encode('utf-8') + message
                sender_message = "[You] ".encode('utf-8') + message
                client_socket.send(sender_message)
                broadcast(broadcast_message, client_socket)
        except:
            client_socket.close()
            clients.remove(client_socket)
            break

def broadcast(message, sender_socket):
    for client in clients:
        if client != sender_socket:
            try:
                client.send(message)
            except:
                client.close()
                clients.remove(client)

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 60601))
    server_socket.listen()
    print(f'Server started and is listening on port 60601')

    while True:
        client_socket, client_address = server_socket.accept()
        print(f'New connection established with client from {client_address}')
        clients.append(client_socket)
        threading.Thread(target=handle_client, args=(client_socket, client_address)).start()

if __name__ == "__main__":
    start_server()
