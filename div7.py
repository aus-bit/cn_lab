import socket
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(('localhost',1246))
print("server waits")
data,addr=s.recvfrom(1024)
n=int(data.decode())
if n%7==0:
    msg="Divisble"
else:
    msg="Non"
s.sendto(msg.encode(),addr)
s.close