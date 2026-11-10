import socket
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
print("Server waits")
s.bind(('localhost',1256))
data,addr=s.recvfrom(1024)
n=int(data.decode())
a, b = 0, 1
fib= []

for i in range(n):
    fib.append(str(a))
    a, b = b, a + b

result = " ".join(fib)
s.sendto(str(result).encode(),addr)
s.close()