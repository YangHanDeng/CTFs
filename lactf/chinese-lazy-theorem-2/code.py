#copied from internet
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

from socket import socket
sock = socket()
sock.connect(('lac.tf', 31111))
tmp=sock.recv(2000).decode()
p=tmp.split('\n')[0]
q=tmp.split('\n')[1]
#print(p)
#print(q)
sock.send('1\n'.encode())
tmp=sock.recv(2000).decode()
sock.send((p+'\n').encode())
tmp=sock.recv(2000).decode()
a1=tmp.split('\n')[0]
sock.send('1\n'.encode())
tmp=sock.recv(2000).decode()
sock.send((q+'\n').encode())
tmp=sock.recv(2000).decode()
a2=tmp.split('\n')[0]
#print(a1)
#print(a2)
p=int(p)
q=int(q)
a1=int(a1)
a2=int(a2)
N=p*q
m1=q #N/p
m2=p #N/q
y1=modinv(m1%p,p)
y2=modinv(m2%q,q)
x0=(y1*m1*a1+y2*m2*a2)%N
sock.send('2\n'.encode())
for i in range(30):
  tmp=sock.recv(2000).decode()
  print(tmp)
  sock.send((str(x0+N*i)+'\n').encode())