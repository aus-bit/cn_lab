import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('localhost',1345))
n=input("Enter:")
s.send(str(n).encode())
data=s.recv(1024)
msg=data.decode()
print("case",msg)
s.close()