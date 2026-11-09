import socket
c=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
n=int(input("Enter no"))
c.connect(('localhost', 1243))
c.send(str(n).encode())
data=c.recv(1024).decode()
print(data)
c.close
