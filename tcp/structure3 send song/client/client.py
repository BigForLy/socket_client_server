############################################
# Transfer MP4
from socket import *
import os
from time import *

# Путь файла
path = "732674668.mp3"
# открыть файл
with open(path, 'rb') as f:
    message = f.read()  # Прочтите это байт
# # Рассчитать размер файла
# file_size = os.path.getsize(path) / 1024 / 1024  # Преобразовано в mb
# # Подключить порт
client = socket(AF_INET, SOCK_STREAM)
# подключиться к серверу
client.connect(("127.0.0.1", 8887))
# print("связаны")
# # Отметить время начала передачи файла
# start_time = time()
# # Отправить байтовый файл на сервер
client.send(message)
# # Отметить конец времени передачи файла
# end_time = time()
# # Рассчитать общее время
# All_time = end_time - start_time
# # Вычислить коэффициент, округленный до ближайших двух
# rate = round(file_size / All_time, 2)  # Рассчитать коэффициент с округлением до двух
# print(f"Файл отправлен {rate} МБ / с")
# # Закрыть соединение
client.close()
# print("Соединение закрыто")
