import socket

n1=int(input("Enter first no: "))
n2=int(input("Enter second no: "))

c=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
c.connect(('localhost',1276))
c.send(str(n1).encode())
c.close()

c=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
c.connect(('localhost',1276))
c.send(str(n2).encode())
c.close()

c=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
c.connect(('localhost',1276))
data=c.recv(1024).decode()
print("Product:",data)
c.close()