import socket
import threading

# List of clients
clients = []

# Broadcasting messages to all connected clients
def broadcast(message, client):
    for c in clients:
        if c != client:
            try:
                c.send(message)
            except:
                clients.remove(c)

# Handling each client
def handle_client(client):
    while True:
        try:
            message = client.recv(1024)
            if message:
                print(f"Message received: {message.decode()}")
                broadcast(message, client)
            else:
                break
        except:
            clients.remove(client)
            break

# Main function to handle incoming clients
def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(('localhost', 12345))
    server.listen(5)
    print("Server started... Waiting for connections.")

    while True:
        client, address = server.accept()
        print(f"Connection established with {address}")
        clients.append(client)
        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()

if __name__ == "__main__":
    start_server()
