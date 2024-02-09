import socket
host = "127.0.0.1"
port = 5000
server = socket.socket()
print("server Socket")
server.bind((host, port))
server.listen()
conn, addr = server.accept()
data = conn.recv(1024).decode()
filename='Hello.txt'
f = open(filename,'rb')
while True:
   l = f.read(1024)
   if not l:
      break
   conn.send(l)
   print('Sent ',str(l))
f.close()
print('File transferred')
conn.close()