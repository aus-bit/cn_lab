import socket
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(('localhost',1235))
print("Server waiting...")
n1,addr=s.recvfrom(1024)
n1=int(n1.decode())
n2,addr=s.recvfrom(1024)
n2=int(n2.decode())
a=n1*n2
p=n1+n1+n2+n2
s.sendto(str(a).encode(),addr)
s.sendto(str(p).encode(),addr)
s.close