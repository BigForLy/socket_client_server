# UDP server socket
# netstat -ano | findstr :8887 show id process
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('127.0.0.1', 8887))

while True:
    try:
        result = sock.recv(1024)
        print('Message', result.decode('utf-8'))
    except KeyboardInterrupt:
        sock.close()
        break
