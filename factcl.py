import socket
c=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
c.connect(('localhost',1287))
n=int(input("Enter a number: "))
c.send(str(n).encode())
data=c.recv(1024).decode()
print("Factorial:",data)
c.close()