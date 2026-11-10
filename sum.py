import socket
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
print("Server waits..........")
s.bind(('localhost',1243))
data,addr=s.recvfrom(1024)
n=int(data.decode())
sum=(n*(n+1))/2
avg=sum/n
s.sendto(str(sum).encode(),addr)
s.sendto(str(avg).encode(),addr)
s.close()