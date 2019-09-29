import socket

class TCPsocket:
    def __init__(self, port, ip):
        self.serverName = ip
        self.serverPort = port 
        self.Socket = socket.socket(AF_INET, SOCK_STREAM)


    def send_message(self, message):
        self.Socket.connect((self.serverName, self.serverPort))
        self.Socket.send(message)
        response = self.Socket.recv(2048)
        self.Socket.close()

    def listen(self, message):
        self.Socket.bind(("",serverPort))
        self.Socket.listen(1)
        print("The server is ready to receive")
        while(raw_input() != 'C'):
            connectionSocket, addr = Socket.accept()
            receivedMessage = connectionSocket.recv(1024)
            connectionSocket.send(capitalizedSentence)
            connectionSocket.close()



        
