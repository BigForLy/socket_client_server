# TCP client socket
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('127.0.0.1', 8887))
sock.send('Test фыф'.encode('utf-8'))
sock.close()
