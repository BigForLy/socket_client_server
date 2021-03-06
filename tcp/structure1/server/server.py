# TCP server socket
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('127.0.0.1', 8887))
sock.listen(5)

while True:
    try:
        client, address = sock.accept()
        result = client.recv(1024)
        client.close()
        print('Message', result.decode('utf-8'))
    except KeyboardInterrupt:
        sock.close()
        break
