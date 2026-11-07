import socket
c=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
msg=input("Enter sentence")
c.sendto(msg.encode(),('localhost',1278))
data,addr=c.recvfrom(1024)
print("translated sentence:",data.decode())
c.close()