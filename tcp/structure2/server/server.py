# TCP server socket
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('127.0.0.1', 8887))
sock.listen(5)

while True:
    try:
        client, address = sock.accept()
        temp = client.recv(128)
        result = client.recv(int(temp.decode('utf-8')))
        client.close()
        with open("test1.txt", "wb") as file:
            file.write(result)
    except KeyboardInterrupt:
        sock.close()
        break
