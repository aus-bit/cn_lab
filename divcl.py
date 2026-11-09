import socket
c=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
n=int(input("Enter no"))
c.sendto(str(n).encode(), ('localhost', 1235))

data, addr = c.recvfrom(1024)
print(data.decode())
c.close()
