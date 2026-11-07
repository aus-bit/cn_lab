import socket
import json
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('localhost',12345))
s.listen(1)
print("Server is waiting")
conn,adrr=s.accept()
print("Client connected")
data=conn.recv(4096).decode()
matrix=json.loads(data)
n=len(matrix)
diagonal=True
upper=True
lower=True
for i in range(n):
    for j in range(n):
        if i!=j and matrix[i][j]!=0:
            diagonal=False
        if i>j and matrix[i][j]!=0:
            upper=False
        if i<j and matrix[i][j]!=0:
            lower=False
if diagonal:
     result="Diagonal Matrix"
elif upper:
     result="Upper Matrix"
elif lower:
     result="Lower Matrix"
else:
     result="Non"
conn.send(result.encode())
print("Matrix type:",result)
conn.close()
s.close()
