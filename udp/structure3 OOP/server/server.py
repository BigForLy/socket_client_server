import socketserver


class ThreadingTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass


class EchoUDPHandler(socketserver.BaseRequestHandler):

    def handle(self) -> None:
        data, socket = self.request
        print(f'Address: {self.client_address[0]}')
        print(f'Data: {data.decode()}')
        socket.sendto(data, self.client_address)


if __name__ == '__main__':
    with ThreadingTCPServer(('0', 8887), EchoUDPHandler) as server:
        server.serve_forever()
