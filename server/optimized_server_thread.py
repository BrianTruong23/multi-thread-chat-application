import socket
import threading
import time
from concurrent.futures import ThreadPoolExecutor

# Function to handle client connections
def handle_client(client_socket, addr):
    print(f"New connection: {addr}")
    while True:
        try:
            start_time = time.time()  # Start time for latency measurement
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                break
            print(f"{addr}: {message}")
            broadcast(message, client_socket)
            # Send a proper HTTP response back to the client
            response = (
                "HTTP/1.1 200 OK\r\n"
                "Content-Type: application/json\r\n"
                "Content-Length: 17\r\n"
                "\r\n"
                '{"status": "ok"}'
            )
            client_socket.send(response.encode('utf-8'))
            end_time = time.time()  # End time for latency measurement
            latency = (end_time - start_time) * 1000  # Convert to milliseconds
            print(f"Latency for {addr}: {latency} ms")
            # Append latency value with a newline
            with open('latency_thread.txt', "a") as f:
                f.write(f"{latency}\n")
        except Exception as e:
            print(f"Error: {e}")
            break
    client_socket.close()

# Function to broadcast messages to all clients
def broadcast(message, client_socket):
    for client in clients:
        if client != client_socket:
            try:
                client.send(message.encode('utf-8'))
            except:
                client.close()
                clients.remove(client)

# Main function to start the server
def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('127.0.0.1', 12345))
    server_socket.listen(5)
    print("Server started on port 12345")

    with ThreadPoolExecutor(max_workers=10) as executor:
        while True:
            client_socket, addr = server_socket.accept()
            clients.append(client_socket)
            executor.submit(handle_client, client_socket, addr)

clients = []
start_server()
