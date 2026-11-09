import socket
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
msg=input("Enter string")
s.sendto(msg.encode(),('localhost',1298))
data,addr=s.recvfrom(1024)
print("Length:",data.decode())
s.close()