
import socket
import threading

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('localhost', 1234))
s.listen(5)

clients = []

def broadcast(msg, sender):
    for client in clients:
        if client != sender:
            client.send(msg)

def handle_client(c, addr):
    print("Connected:", addr)

    while True:
        try:
            msg = c.recv(1024).decode()

            if not msg:
                break

            print("Client:", msg)
            broadcast(msg.encode(), c)

        except:
            break

    clients.remove(c)
    c.close()
    print("Client disconnected:", addr)

print("Server waiting...")

while True:
    c, addr = s.accept()
    clients.append(c)

    threading.Thread(target=handle_client,
                     args=(c, addr)).start()
