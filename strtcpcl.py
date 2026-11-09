
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(('localhost', 1234))

msg = input("Enter msg: ")

s.send(msg.encode())

data = s.recv(1024).decode()

print("Length", data)

s.close()

