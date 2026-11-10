import socket
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
msg=input("enter:")
s.sendto(str(msg).encode(),('localhost',1245))
data,addr=s.recvfrom(1024)
count=data.decode()
print("count",count)