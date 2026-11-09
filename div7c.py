import socket
c=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
n=int(input("Enter No:"))
c.sendto(str(n).encode(),('localhost',1246))
data,addr=c.recvfrom(1024)
print(data.decode())
c.close()