import socket
import threading

class Server:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((self.host, self.port))
        self.server.listen(5)  # Listen for incoming connections
        print(f"Server is listening on {self.host}:{self.port}")

        self.clients = []  # List to store connected client sockets

    def handle_client(self, client_socket):
        while True:
            try:
                data = client_socket.recv(1024).decode()
                if not data:
                    print(f"Client {client_socket.getpeername()} disconnected")
                    self.clients.remove(client_socket)
                    client_socket.close()
                    break
                print(f"Received from {client_socket.getpeername()}: {data}")
                # You can add your data processing logic here

                resp = input("Enter response: ")

                client_socket.send(resp.encode())
            except Exception as e:
                print(f"Error handling client {client_socket.getpeername()}: {e}")
                break

    def _start(self):
        while True:
            print("Waiting for a connection...")
            self.server.listen(5)
            client_socket, client_address = self.server.accept()
            print(f"Accepted connection from {client_address}")
            self.clients.append(client_socket)

            # Create a new thread to handle the client
            client_thread = threading.Thread(target=self.handle_client, args=(client_socket,))
            client_thread.start()
    def start(self):
        t = threading.Thread(target=self._start, daemon=True)
        t.start()

        t.join()



if __name__ == "__main__":
    server = Server("127.0.0.1", 65053)  # Listen on all available network interfaces
    server.start()
