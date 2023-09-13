import socket
import threading
from time import sleep


class LANServer:
    def __init__(self, port, respondFunc):
        # get ip of current machine
        self.host = socket.gethostbyname(socket.gethostname())
        self.port = port
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((self.host, self.port))
        self.server.listen(5)  # Listen for incoming connections
        print(f"Server is listening on {self.host}:{self.port}")

        self.clients = []  # List to store connected client sockets

        self.respondFunc = respondFunc

        self.open = True

    def handle_client(self, client_socket):
        while True:
            try:
                data = client_socket.recv(1024).decode()
                if not data:
                    print(f"Client {client_socket.getpeername()} disconnected")
                    self.clients.remove(client_socket)
                    client_socket.close()
                    break
                print(f"Server received data from {client_socket.getpeername()}: {data}\n")

                resp = self.respondFunc(data)

                print(f"Server sending response to {client_socket.getpeername()}: {resp}")
                client_socket.send(resp.encode())
            except Exception as e:
                try:
                    print(f"Error handling client {client_socket.getpeername()}: {e}")
                    break
                except Exception as e:
                    print(f"Client Disconnected")
                    break

    def _start(self):
        while True:
            if not self.open:
                print("Closing server...")
                break

            try:
                print("Waiting for a connection...\n")
                self.server.listen(5)
                client_socket, client_address = self.server.accept()
                print(f"Accepted connection from {client_address}")
                self.clients.append(client_socket)

                # Create a new thread to handle the client
                client_thread = threading.Thread(target=self.handle_client, args=(client_socket,))
                client_thread.start()
            except Exception as e:
                if self.open:
                    print(f"Error accepting connection: {e}")
                else:
                    print("Server closed")
                    break


    def start(self):

        self.open = True

        self.main_thread = threading.Thread(target=self._start)
        self.main_thread.start()


        # run thread until self.close is called


    def close(self):
        self.open = False

        self.server.close()
        for c in self.clients:
            c.close()



if __name__ == "__main__":
    server = LANServer(65053, lambda e: "")  # Listen on all available network interfaces
    server.start()
