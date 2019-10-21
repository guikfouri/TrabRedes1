from socket import *

def HTTPresponse(receivedMessage):
    print(receivedMessage)
    return bytearray("Mensagem recebida", 'utf-8')

#def FTPresponse(receivedMessage):

class meu_socket:

    def __init__(self, serverIp, serverPort, protocol):
        self.serverIp = serverIp
        self.serverPort = serverPort 
        self.protocol = protocol
        if self.protocol == "UDP" :
            self.Socket = socket(AF_INET, SOCK_DGRAM)
        elif self.protocol == "TCP" :
            self.Socket = socket(AF_INET, SOCK_STREAM)

    def send_message(self, message):
        self.Socket.connect((self.serverIp, self.serverPort))
        self.Socket.send(message)
        response = self.Socket.recv(2048)
        self.Socket.close()
        return response

    def listen(self):
        if self.protocol == "UDP" :
            listenTCP()
        elif self.protocol == "TCP" :
            listenUDP()

    def listenUDP(self):
        self.Socket.bind(('', self.serverPort))
        print("The server is ready to receive")
        while(raw_input() != 'C'):
            receivedMessage, clientAddress = Socket.recv(2048)

            if self.protocol == "HTTP" :
                responseMessage = HTTPresponse(receivedMessage)
            elif self.protocol == "FTP" :
                responseMessage = FTPresponse(receivedMessage)

            Socket.sendto(responseMessage, clientAddress)

    def listenTCP(self):
        self.Socket.bind(('', self.serverPort))
        self.Socket.listen(1)
        print("The server is ready to receive")
        while(input() != 'C'):
            connectionSocket, addr = Socket.accept()
            receivedMessage = connectionSocket.recv(1024)
            print(receivedMessage)

            if self.protocol == "HTTP" :
                responseMessage = HTTPresponse(receivedMessage)
            elif self.protocol == "FTP" :
                responseMessage = FTPresponse(receivedMessage)
                
            connectionSocket.send(responseMessage)
            connectionSocket.close()

    


        
