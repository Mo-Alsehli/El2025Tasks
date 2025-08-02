import socket
import time
import threading

def client_worker(client_id, host='localhost', port=12345):
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)
        client_socket.connect((host, port))
        print(f"[Client {client_id}] Connected To Server {host}: {port}")

        messages = [
                    f"[Client {client_id}] hello server", 
                    f"[Client {client_id}] how are you", 
                    f"[Client {client_id}] good bye"
                    ]

        for m in messages:
            client_socket.send(m.encode())
            print(f"Sent: {m}")

            response = client_socket.recv(1024).decode()
            print(f"Recieved: {response}")

            time.sleep(1)
    except ConnectionRefusedError:
        print("Faild to connect to server")
    finally:
        client_socket.close()
        print(f"[Client {client_id}] Disconnected")


# Handle multiple clients
def start_multiple_clients(num_clients=3):
    threads = []

    for i in range(num_clients):
        t = threading.Thread(
            target=client_worker,
            args=(i,)
        )
        t.start()
        threads.append(t)
        time.sleep(0.5)

    for t in threads:
        t.join()

if __name__ == "__main__":
    start_multiple_clients(num_clients=5)