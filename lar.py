import socket
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
print("serveer wait")
s.bind(('localhost',1345))
data,addr=s.recvfrom(1024)
n=int(data.decode())
largest = 0

while n > 0:
    digit = n % 10

    if digit > largest:
        largest = digit

    n //= 10

result = str(largest)
s.sendto(str(result).encode(),addr)
s.close()