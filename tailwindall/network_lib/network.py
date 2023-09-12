import threading


def handle_client(client):
    while True:
        try:
            message = client.receive()
            if not message:
                break
            print(f"Received from {client.host}:{client.port}: {message}")
            # You can add your logic to process the received message here
        except Exception as e:
            print(f"Error handling client {client.host}:{client.port}: {e}")
            break

def _handle_clients(clients, server):
    thread = threading.Thread(target=handle_clients, args=(clients,server,), daemon=True)
    thread.start()


def handle_clients(clients,server):
    threads = []
    for c in clients:
        thread = threading.Thread(target=handle_client, args=(c,))
        thread.start()
        threads.append(thread)

    thread = threading.Thread(target=wait_for_threads, args=(threads, clients, server) ,daemon=True)
    thread.start()

def wait_for_threads(threads, clients, server):
    for t in threads:
        t.join()

    for c in clients:
        c.close()
    server.close()
