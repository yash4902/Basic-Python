import socket

s = socket.socket()
host = '127.0.0.1'
port = 5000

s.connect((host,port))
s.send("hello server".encode())

with open("Hello.txt",'wb') as f:
    while True:
        print("receiving data...")
        data = s.recv(1024)
        if not data:
            break
        f.write(data)
f.close()
print("Succesfully Received")
s.close()
print("connection closed")