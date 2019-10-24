from TCPsocket import meu_socket

if __name__ == "__main__":
    server = meu_socket("127.0.0.1", 17000, "TCP")
    while 1:
        server.listenTCP()