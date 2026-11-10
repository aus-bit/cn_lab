import socket
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
n=int(input("enter:"))
s.sendto(str(n).encode(),('localhost',1237))
data,addr=s.recvfrom(1024)
result=data.decode()
print("avg",result)
s.close()