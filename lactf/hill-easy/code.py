from socket import socket
import numpy as np

n=20
def stov(s):
  return np.array([ord(c)-32 for c in s])
def vtos(v):
  return ''.join([chr(v[i]+32) for i in range(n)])
def encrypt(s):
  return vtos(np.matmul(A, stov(s))%95)

sock = socket()
sock.connect(('lac.tf', 31140))
tmp=sock.recv(2000).decode()
f1=tmp.split('\n')[1]
f2=tmp.split('\n')[2]
record=['']*20
for i in range(10):
  base="                    "
  base1=base[:i]+'!'+base[i+1:]
  base2=base[:i+10]+'!'+base[i+11:]
  sock.send((base1+base2+'\n').encode())
  tmp=sock.recv(2000).decode()
  record[i]=tmp.split('\n')[1]
  record[i+10]=tmp.split('\n')[2]
#print(record)

for i in range(20):
  record[i]=stov(record[i])
#print(record)
A = np.asarray(record)
A=A.T
#print(A)
fakeflag2=tmp.split('\n')[7]
f3=encrypt(fakeflag2[:20])
f4=encrypt(fakeflag2[20:])
sock.send((f3+'\n').encode())
tmp=sock.recv(2000).decode()
sock.send((f4+'\n').encode())
tmp=sock.recv(2000).decode()
print(tmp)