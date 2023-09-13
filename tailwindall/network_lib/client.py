import socket

from tailwindall.network_lib import network


class LANClient:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        print(f"Connecting to {self.host}:{self.port}...")

    def connect(self):
        self.client.connect((self.host, self.port))

        print(f"Connected to {self.host}:{self.port}")

    def send(self, data):
        if isinstance(data, network.Request):
            data = str(data)
        self.client.send(data.encode())
        return self.receive()

    def receive(self):
        return self.client.recv(1024).decode()

    def close(self):
        self.client.close()

if __name__ == "__main__":
    client = LANClient(65053)  # Replace SERVER_IP with the actual server's IP address
    client.connect()


    while True:
        msg = input("Enter message: ")
        if msg == "exit":
            break
        response = client.send(msg)

        print("Server response:", response)

    client.close()
