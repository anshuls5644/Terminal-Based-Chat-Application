import socket
import threading

# Handling messages received from the server
def receive_messages(client):
    while True:
        try:
            message = client.recv(1024)
            if message:
                print(message.decode())
        except:
            print("Connection lost.")
            break

# Sending messages to the server
def send_messages(client):
    while True:
        message = input()
        client.send(message.encode())

# Main function to connect to the server and start communication
def start_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('localhost', 12345))

    # Start a thread to receive messages from the server
    threading.Thread(target=receive_messages, args=(client,)).start()

    # Start a thread to send messages to the server
    threading.Thread(target=send_messages, args=(client,)).start()

if __name__ == "__main__":
    start_client()
