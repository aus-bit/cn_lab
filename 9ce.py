
import socket

c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
c.connect(('localhost', 12345))

filename = input("Enter filename: ")
c.send(filename.encode())

data = c.recv(4096).decode()
print("\nServer Response:")
print(data)

c.close()
