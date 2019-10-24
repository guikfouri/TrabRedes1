from socket import *
from datetime import datetime


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
        return response.decode()

    def listen(self):
        if self.protocol == "UDP" :
            self.listenTCP()
        elif self.protocol == "TCP" :
            self.listenUDP()

    def listenUDP(self):
        self.Socket.bind(('', self.serverPort))
        print("The server is ready to receive")
        while(input() != 'C'):
            receivedMessage, clientAddress = self.Socket.recv(2048)

            responseMessage = HTTPresponse(receivedMessage)

            self.Socket.sendto(responseMessage, clientAddress)

    def listenTCP(self):
        self.Socket.bind(('', self.serverPort))
        self.Socket.listen(1)
        print("The server is ready to receive\n")
        while True:
            connectionSocket, addr = self.Socket.accept()
            receivedMessage = connectionSocket.recv(2048)
            receivedMessage = receivedMessage.decode()
            print("Connection accepted: " + receivedMessage)
            requisicao = receivedMessage.split()

            responseMessage = HTTPresponse(receivedMessage) 
            connectionSocket.send(responseMessage)
            connectionSocket.close()
                
                
def HTTPresponse(receivedMessage):
    receivedMessage = receivedMessage.split()
    now = datetime.now()
    days = ('Mon, ', 'Tue, ', 'Wed, ', 'Thu, ', 'Fri, ', 'Sat, ', 'Sun, ')
    months = ('Jan ', 'Feb ', 'Mar ', 'Apr ', 'May ', 'Jun ', 'Jul ', 'Aug ', 'Sept ', 'Oct ', 'Nov ', 'Dec ')
    try:
        if (receivedMessage[0] == 'GET'):
            path = './Arquivos_teste/' + receivedMessage[1]
            arquivo = open(path,'r')
            arquivo_string = arquivo.read()
            response = """HTTP/1.1 200 OK
            Connection: close 
            Date:""" + days[now.weekday()] + str(now.day()) + ' ' + months[now.month()] + str(now.year()) + ' ' + str(now.hour()) + ':' + str(now.minute()) + ':' + str(now.second()) + """GMT
            Server: MyServer/1.0 (Debian)
            Last-Modified: 
            Content-Length: 
            Content-Type:
            
            """
            # connectionSocket.send(str.encode(response))
            print('Arquivo '+receivedMessage[1]+' encontrado.\n')
            arquivo.close()

    except FileNotFoundError:
        print('Arquivo não encontrado.\n')
        response = """HTTP/1.1 404 File Not Found
            Connection: close
            Date: """ + days[now.weekday()] + now.day() + ' ' + months[now.month()] + now.hour() + ':' + now.minute() + ':' + now.second() + """GMT
            Server: MyServer/1.0 (Debian)
            
            """
        # connectionSocket.send(str.encode(response))

    except:
        print('Requisição inválida.\n')
        response = """HTTP/1.1 500 Bad Request
            Connection: close
            Date: """ + days[now.weekday()] + now.day() + ' ' + months[now.month()] + now.hour() + ':' + now.minute() + ':' + now.second() + """GMT
            Server: MyServer/1.0 (Debian)
            
            """
        # connectionSocket.send(str.encode(response))

    return str.encode("Mensagem recebida")

    


        
