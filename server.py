import socket

s = socket.socket()             #if socket() parameters left blank, default arguments are IPv4 and TCP
print('Socket created')

s.bind(('localhost',9999))

s.listen(3)                     #listens for up to 3 connections, more get dropped
print('waiting for connections')

while True:
    c, addr = s.accept()
    name = c.recv(1024).decode()
    print('Connected with ', addr, name)



    c.send(bytes('Welcome to server','utf-8'))

    c.close()