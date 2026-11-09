import socket

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('localhost',1276))
s.listen(2)

print("Server waiting")

conn,addr=s.accept()
n1=int(conn.recv(1024).decode())
conn.close()

conn,addr=s.accept()
n2=int(conn.recv(1024).decode())
conn.close()

result=n1*n2

conn,addr=s.accept()
conn.send(str(result).encode())
conn.close()

s.close()