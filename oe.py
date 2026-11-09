import socket
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
print("Server Waiting....")
s.bind(('localhost',1234))
data,addr=s.recvfrom(1024)
n=int(data.decode())
if n%2==0:
    msg="even"
else:
    msg="odd"
s.sendto(msg.encode(),addr)
s.close()