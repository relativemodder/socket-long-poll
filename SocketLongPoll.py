import socket
import os
import time
sock = socket.socket()
sock.bind(('', 9090))

tс = 0


while True:
    sock.listen(1)
    conn, addr = sock.accept()
    while True:
        data = conn.recv(1024)
        if not data:
            break
        while True:
            try:
                t = os.path.getmtime("pollFile.txt")
            except:
                time.sleep(0.2)
                t = os.path.getmtime("pollFile.txt")
            if(t>tс):
                tс=t
                time.sleep(0.2)
                f = open("pollFile.txt", "r")
                content = f.read(99999999)
                f.close()
                conn.send(("changed file to "+content).encode("utf-8"))
                break
        
    conn.close()