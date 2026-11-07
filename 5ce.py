import socket
import json
import random
n=int(input("Size of matric:"))
matrix=[]
for i in range(n):
    row=[]
    for j in range(n):
        row.append(random.randint(1,50))
    matrix.append(row)
    print("Generated Matrix")
    for row in matrix:
        print(row)
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('localhost',12345))
data=json.dumps(matrix)
s.send(data.encode())
result=s.recv(1024).decode()
print("Result",result)
s.close()
