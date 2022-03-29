# Transfer MP4
from socket import *
from time import *
import os

start_time = time()
ip = "127.0.0.1"
port = 8887
server = socket(AF_INET, SOCK_STREAM)
server.bind((ip, port))
server.listen(5)
print(f"[*] прослушивает локальный порт {port}")
while True:
    # Ожидание в этой позиции, номер порта прослушивания
    connection, addr = server.accept()
    if connection:
        print("[*] не связан ни с одним клиентом", end='\r')
    print(f"[*] Подключиться к клиенту {addr[0]}: {addr[1]}")

    while True:
        # Принять размер сокета
        data = connection.recv(1024)
        if not data:
            break
        path = "732674668.mp3"
        with open(path, 'ab') as f:
            f.write(data)
    file_size = os.path.getsize(path)  # Единица - B (байт) (байт)
    connection.close()
    print("[*] Соединение было закрыто, ожидает повторного соединения")
    end_time = time()
    AlL_time = end_time - start_time
    print(f"Сервер уже работает {round(AlL_time, 1)} s")
    print(f"Файл {round(file_size / 1024 / 1024, 2)} mb")
