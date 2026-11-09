
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

n = int(input("Enter no: "))

s.sendto(str(n).encode(), ('localhost', 1234))

data, addr = s.recvfrom(1024)

msg = data.decode()

print("No is", msg)

s.close()
