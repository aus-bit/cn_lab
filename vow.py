import socket
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
print("server waits.......")
s.bind(('localhost',1245))
data,addr=s.recvfrom(1024)
msg=data.decode()
count=0
for ch in msg:
    if ch in  "aeiouAEIOU":
       count+=1
s.sendto(str(count).encode(),addr)
s.close()