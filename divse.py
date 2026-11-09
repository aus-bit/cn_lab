import socket
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
print("server waiting")
s.bind(('localhost',1235))
data,addr=s.recvfrom(1024)
n=int(data.decode())
if n%3 == 0 and n%5 == 0:
    msg="divisble"
else:
    msg="not divisible"
s.sendto(msg.encode(),addr)
s.close