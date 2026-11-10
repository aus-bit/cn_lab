import socket
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
print("Server waits..........")
s.bind(('localhost',1243))
data,addr=s.recvfrom(1024)
n=int(data.decode())
count=0
for i in range(1,n+1):
    if n%i==0:
        count+=1
if n==2:
    msg="prime"
else:
    msg = "Not Prime"

s.sendto(msg.encode(), addr)

s.close()
