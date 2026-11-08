import socket
from datetime import datetime

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('localhost', 1238))

print("Time server waiting...")

while True:
    data, addr = s.recvfrom(1024)
    t = str(datetime.now())
    s.sendto(t.encode(), addr)
