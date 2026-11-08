import socket
c=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
c.sendto("Time request".encode(),('localhost',1238))
data,addr=c.recvfrom(1024)
print("Server time:", data.decode())
c.close