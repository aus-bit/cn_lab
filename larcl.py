import socket
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
n=int(input("Enter:"))
s.sendto(str(n).encode(),('localhost',1345))
data,addr=s.recvfrom(1024)
result=data.decode()
print("largest",result)
s.close()