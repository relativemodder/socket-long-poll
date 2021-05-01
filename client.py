import socket

while True:
    sock = socket.socket() # New socket
    sock.connect(('localhost', 9090)) # connectin

    sock.send('hello, world!'.encode("utf-8")) # request to server

    data = sock.recv(1024) # receivin data
    sock.close() # close ur socket 4 u uwu

    print(data) # actually print
