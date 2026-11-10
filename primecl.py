
import socket

c = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

n = int(input("Enter number: "))

c.sendto(str(n).encode(), ('localhost', 1243))

data, addr = c.recvfrom(1024)

print("Result:", data.decode())

c.close()
