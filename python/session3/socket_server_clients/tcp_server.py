import socket
import threading


def handle_client(client_socket:socket.socket, address):
    print(f"Connection established with {address}")
    client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)

    try:
        while True:
            data = client_socket.recv(1024).decode()
            if not data:
                break

            print(f"Recived from {address}: {data}")

            # Echo response to client again.
            response = f"Echo: {data}"
            client_socket.send(response.encode())
    except Exception as e:
        print(f"Error handling client: {e}")
    finally:
        client_socket.close()
        print(f"Connections with address: {address} Closed")


def start_server(host='localhost', port=12345):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Allow socket reuse.
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    server_socket.bind((host, port))
    server_socket.listen(5)
    try:
        while True:
            client_socket, address = server_socket.accept()

            # handle client in separate thread
            client_thread = threading.Thread(
                target=handle_client,
                args=(client_socket, address)
            )

            client_thread.daemon = True
            client_thread.start()
    except KeyboardInterrupt:
        print("\n Server shut down")
    finally:
        server_socket.close()

if __name__ == "__main__":
    start_server()
    
