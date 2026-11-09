import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('localhost',1243))
s.listen(1)
print("Server waiting.........")
conn,addr=s.accept()
data=conn.recv(1024).decode()
n=data
if n == n[::-1]:
   msg="palindrome"
else:
   msg="no"
conn.send(msg.encode())
conn.close()
s.close()