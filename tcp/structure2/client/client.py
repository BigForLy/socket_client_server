# TCP client socket
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('127.0.0.1', 8887))
with open('test1.txt', 'r') as file:
    p = file.read()
    l = str(file.__sizeof__())
    sock.send(l.encode('utf-8'))
    sock.send(p.encode('utf-8'))
sock.close()
