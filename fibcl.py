import socket
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
n=int(input("Enter no"))
s.sendto(str(n).encode(),('localhost',1256))
data,addr=s.recvfrom(1024)
result=data.decode()
print("Fib",result)
s.close()