import socket
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
print("server waiting.....")
s.bind(('localhost',1298))
data,addr=s.recvfrom(1024)
msg=data.decode()
length=len(msg)
s.sendto(str(length).encode(),addr)
s.close()
