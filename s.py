import socket
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
print("Server waits..........")
s.bind(('localhost',1249))
data,addr=s.recvfrom(1024)
n=int(data.decode())
a=n*n
c=n*n*n
s.sendto(str(a).encode(),addr)
s.sendto(str(c).encode(),addr)
s.close()
