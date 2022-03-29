# UDP client socket
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto('Test фыф'.encode('utf-8'), ('127.0.0.1', 8887))
sock.close()
