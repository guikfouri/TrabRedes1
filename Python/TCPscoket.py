import socket

def HTTPresponse(receivedMessage):

def FTPresponse(receivedMessage):

class TCPsocket:

    def __init__(self, serverIp, serverPort, protocol):
        self.serverIp = ip
        self.serverPort = port 
        self.protocol = protocol
        if self.protocol == "UDP" :
            self.Socket = socket.socket(AF_INET, SOCK_DGRAM)
        elif self.protocol = "TCP" :
            self.Socket = socket.socket(AF_INET, SOCK_STREAM)

    def send_message(self, message):
        self.Socket.connect((self.serverName, self.serverPort))
        self.Socket.send(message)
        response = self.Socket.recv(2048)
        self.Socket.close()

    def listen(self, message):
        if self.protocol == "UDP" :
            listenTCP(message)
        elif self.protocol == "TCP" :
            listenUDP(message)

    def listenUDP(self, message, protocol):
        self.Socket.bind(("",serverPort))
        print("The server is ready to receive")
        while(raw_input() != 'C'):
            receivedMessage, clientAddress = Socket.recv(2048)

            if protocol == "HTTP" :
                responseMessage = HTTPresponse(receivedMessage)
            elif protocol == "FTP" :
                responseMessage = FTPresponse(receivedMessage)

            Socket.sendto(responseMessage, clientAddress)

    def listenTCP(self, message):
        self.Socket.bind(("",serverPort))
        self.Socket.listen(1)
        print("The server is ready to receive")
        while(raw_input() != 'C'):
            connectionSocket, addr = Socket.accept()
            receivedMessage = connectionSocket.recv(1024)

            if protocol == "HTTP" :
                responseMessage = HTTPresponse(receivedMessage)
            elif protocol == "FTP" :
                responseMessage = FTPresponse(receivedMessage)
                
            connectionSocket.send(responseMessage)
            connectionSocket.close()

    


        
