import socket
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
n=int(input("Enter no"))
s.sendto(str(n).encode(),('localhost',1249))
data,addr=s.recvfrom(1024)

a=data.decode()
print("square",a)
data,addr=s.recvfrom(1024)
c=data.decode()

print("cube",c)
s.close()