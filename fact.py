import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print("Server connected")
s.bind(('localhost',1287))
s.listen(1)
conn,addr=s.accept()
data=conn.recv(1024).decode()
n=int(data)
fact=1
for i in range(1,n+1):
    fact=fact*i
conn.send(str(fact).encode())
conn.close()
s.close()