
import socket
import threading
import os

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('localhost',12345))
s.listen(5)

def handle_client(c, addr):
    print("Connected:", addr)

    filename = c.recv(1024).decode()
    pid = os.getpid()

    if os.path.exists(filename):
        f = open(filename, 'r')
        data = f.read()
        f.close()

        msg = "PID: " + str(pid) + "\nFile Contents:\n" + data
    else:
        msg = "PID: " + str(pid) + "\nFile not found"

    c.send(msg.encode())
    c.close()

print("Server waiting...")

while True:
    c, addr = s.accept()
    threading.Thread(target=handle_client, args=(c, addr)).start()
