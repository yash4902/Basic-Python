import socket 
host = '127.0.0.1'
port = 3000
server = socket.socket()
server.bind((host,port))
server.listen()
conn, addr = server.accept()
print("Connection from: "+ str(addr))
while True:
    data = conn.recv(4096).decode()
    if not data:
        break
    data = str(data)
    print("from client"+ str(data))
    data = input("type message: ")
    conn.send(data.encode())
conn.close()



