from socket import *
from datetime import datetime

def app_protocol(receivedMessage):
    lista = receivedMessage.split()
    try:
        lista[2] == 'HTTP/1.1'
        return 'HTTP'
    except:
        return 'FTP'


def HTTPresponse(receivedMessage):
    now = datetime.now()
    days = ('Mon, ', 'Tue, ', 'Wed, ', 'Thu, ', 'Fri, ', 'Sat, ', 'Sun, ')
    months = ('Jan ', 'Feb ', 'Mar ', 'Apr ', 'May ', 'Jun ', 'Jul ', 'Aug ', 'Sept ', 'Oct ', 'Nov ', 'Dec ')

    if type(receivedMessage) == 'bytes':
        receivedMessage = receivedMessage.decode()
    receivedMessage = receivedMessage.split()

    try:
        if receivedMessage[0] == 'GET':
            path = './Arquivos_server/' + receivedMessage[1]
            arquivo = open(path,'r')
            arquivo_string = arquivo.read()
            response = """HTTP/1.1 200 OK
Connection: close 
Date: """ + days[now.weekday()] + str(now.day) + ' ' + months[now.month] + str(now.year) + ' ' + str(now.hour) + ':' + str(now.minute) + ':' + str(now.second) + """ UTC-3            
Server: MyServer/1.0 (Debian)
Last-Modified: 
Content-Length: 
Content-Type:
            
""" + arquivo_string
            print('Arquivo '+receivedMessage[1]+' encontrado.\n')
            arquivo.close()

    except FileNotFoundError:
        print('Arquivo não encontrado.\n')
        response = """HTTP/1.1 404 File Not Found
Connection: close
Date: """ + days[now.weekday()] + str(now.day) + ' ' + months[now.month] + str(now.year) + ' ' + str(now.hour) + ':' + str(now.minute) + ':' + str(now.second) + """ UTC-3            
Server: MyServer/1.0 (Debian) 

"""
        return str.encode('0')

    except:
        print('Requisição inválida.\n')
        response = """HTTP/1.1 500 Bad Request
Connection: close
Date: """ + days[now.weekday()] + str(now.day) + ' ' + months[now.month] + str(now.year) + ' ' + str(now.hour) + ':' + str(now.minute) + ':' + str(now.second) + """ UTC-3            
Server: MyServer/1.0 (Debian)
            
 """
        return str.encode('0')

    return str.encode(response)

def FTPresponse(receivedMessage):

    # o cliente pode apenas permanecer em Arquivos_server
    path = '../Arquivos_server/'
    requisicao = receivedMessage.split()
    comando = requisicao[0]
    fin = 0
    if comando == 'QUIT':
        fin = 1
        response = ''

    # RETR {PATH/ARQUIVO_REMOTO}
    elif comando == 'RETR':
        caminho = requisicao[1]
        if '..' in caminho:
            print('Acces denied for:'+ caminho + '\n')
            response = '550 Acces denied\r\n'
        else:
            path += caminho
            arquivo = open(path,'r')
            arquivo_string = arquivo.read()
            response = '200 ok\r\n' + arquivo_string

    # STOR {PATH/ARQUIVO_LOCAL} {PATH_SERVIDOR}
    elif comando == 'STOR':
        pass

    # LIST {PATH_SERVIDOR}
    elif comando == 'LIST':
        pass

    # DELE {PATH_SERVIDOR/ARQUIVO_REMOTO}
    elif comando == 'DELE':
        pass


    return str.encode(response), fin
    


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
            
            Socket.sendto(responseMessage, clientAddress)

    def listenTCP(self):
        self.Socket.bind(('', self.serverPort))
        self.Socket.listen(1)
        print("The server is ready to receive\n")
        while True:
            connectionSocket, addr = self.Socket.accept()
            receivedMessage = connectionSocket.recv(2048)
            receivedMessage = receivedMessage.decode()
            print("Connection accepted: " + receivedMessage)
            if app_protocol(receivedMessage) == 'HTTP':
                response = HTTPresponse(receivedMessage)
                connectionSocket.send(response)
                connectionSocket.close()
            else:
                # No FTP, o connectionSocket será o socket para troca
                # de comandos. Ele não enviará os dados.
                response, fin = FTPresponse(receivedMessage)
                
                # Criar socket de envio de dados
                socketDados = meu_socket("127.0.0.1", 27000, "TCP")
                socketDados.send_message(receivedMessage)
                socketDados.close()


                if fin == 1:
                    connectionSocket.close()
                
                

    


        
