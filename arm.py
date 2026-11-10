import socket
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
print("Server waits..........")
s.bind(('localhost',1237))
data,addr=s.recvfrom(1024)
n=int(data.decode())
temp = n
total = 0
power = len(str(n))

while temp > 0:
    digit = temp % 10
    total += digit ** power
    temp //= 10

if total == n:
    result = "Armstrong Number"
else:
    result = "Not Armstrong Number"
s.sendto(str(result).encode(),addr)
s.close()