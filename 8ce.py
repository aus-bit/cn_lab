
import socket
import threading

c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
c.connect(('localhost', 1234))

def receive():
    while True:
        try:
            msg = c.recv(1024).decode()
            print("\nReceived:", msg)
        except:
            break

threading.Thread(target=receive, daemon=True).start()

while True:
    msg = input("Enter message: ")
    c.send(msg.encode())
