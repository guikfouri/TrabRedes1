from socket import *
from datetime import datetime

#def app_protocol(receivedMessage)
#def HTTPresponse(receivedMessage)
#def FTPresponse(receivedMessage)

class meu_socket:

    def __init__(self, serverIp, serverPort, protocol):
        self.serverIp = serverIp
        self.serverPort = serverPort 
        self.protocol = protocol
    
        if self.protocol == "UDP" :
            self.Socket = socket(AF_INET, SOCK_DGRAM)
        elif self.protocol == "TCP" :
            self.Socket = socket(AF_INET, SOCK_STREAM)

    def connect(self):
        self.Socket.connect((self.serverIp, self.serverPort))

    def close(self):
        self.Socket.close()

    def send_message(self, message, i):
        self.Socket.send(message)
        message = message.decode()
        message = message.split()

        if message[0] == 'RETR':
            data_socket = meu_socket("127.0.0.1", 19000 + i, "TCP")
            arquivo = data_socket.receiveData()
            path = './Arquivos_client/' + message[1]
            arq = open(path, 'w')
            arq.writelines(arquivo)
            arq.close()
            data_socket.close()

        response = self.Socket.recv(2048)
        return response.decode()

    def send_file(self, file):
        self.Socket.connect((self.serverIp, self.serverPort))
        self.Socket.sendfile(file)
        response = self.Socket.recv(2048)
        #self.Socket.close()
        return response.decode()

    def listen(self):
        if self.protocol == "UDP" :
            self.listenTCP()
        elif self.protocol == "TCP" :
            self.listenUDP()

    def listenUDP(self):
        self.Socket.bind(('', self.serverPort))
        print("The server is ready to receive")
        while True :
            receivedMessage, clientAddress = self.Socket.recv(2048)

            responseMessage = HTTPresponse(receivedMessage)
            
            Socket.sendto(responseMessage, clientAddress)

    def listenTCP(self):
        self.Socket.bind(('', self.serverPort))
        self.Socket.listen(1)
        print("The server is ready to receive\n")
        i = 0
        while True:
            connectionSocket, addr = self.Socket.accept()
            receivedMessage = connectionSocket.recv(2048)
            receivedMessage = receivedMessage.decode()
            print("Connection accepted:\r\n" + receivedMessage + '\r\n')

            if app_protocol(receivedMessage) == 'HTTP':
                response = HTTPresponse(receivedMessage)
                connectionSocket.send(response)
                connectionSocket.close()

            else:
                fin = 0
                while(fin == 0):
                    response, fin = FTPresponse(receivedMessage, i)
                    i += 1
                    connectionSocket.send(response)

                    receivedMessage = connectionSocket.recv(2048)
                    receivedMessage = receivedMessage.decode()
                        
                print("FTP connection closed")
                i = 0
                connectionSocket.close()

    def receiveData(self):
        self.Socket.bind(('', self.serverPort))
        self.Socket.listen(1)
        connectionSocket, addr = self.Socket.accept()
        receivedMessage = connectionSocket.recv(2048)
        receivedMessage = receivedMessage.decode()    
        connectionSocket.send(str.encode("Data received"))
        connectionSocket.close()
        return receivedMessage
                


def app_protocol(receivedMessage):
    lista = receivedMessage.split()

    try:
        if lista[2] == 'HTTP/1.1':
            return 'HTTP'
    except:
        return 'FTP'


def HTTPresponse(receivedMessage):
    now = datetime.now()
    days = ('Mon, ', 'Tue, ', 'Wed, ', 'Thu, ', 'Fri, ', 'Sat, ', 'Sun, ')
    months = ('Jan ', 'Feb ', 'Mar ', 'Apr ', 'May ', 'Jun ', 'Jul ', 'Aug ', 'Sept ', 'Oct ', 'Nov ', 'Dec ')

    if type(receivedMessage) == 'bytes':
        receivedMessage = receivedMessage.decode()
    palavras = receivedMessage.split()

    try:
        if palavras[0] == 'GET':
            path = './Arquivos_server/' + palavras[1]
            arquivo = open(path,'r')
            arquivo_string = arquivo.read()

            response = """HTTP/1.1 200 OK
Connection: close 
Date: """ + days[now.weekday()] + str(now.day) + ' ' + months[now.month] + str(now.year) + ' ' + str(now.hour) + ':' + str(now.minute) + ':' + str(now.second) + """ UTC-3            
Server: MyServer/1.0 (Debian)\r\n\r\n""" + arquivo_string

            print('Arquivo '+palavras[1]+' encontrado.\n')
            arquivo.close()
        
        elif palavras[0] == 'POST':
            path = './Arquivos_server/' + palavras[1]
            arquivo = open(path,'r')
            arquivo_string = arquivo.read()
            corpo = receivedMessage.split('\r\n\r\n')[1]
            #arquivo.writelines(dados)     
            response = """HTTP/1.1 200 OK
Connection: close 
Date: """ + days[now.weekday()] + str(now.day) + ' ' + months[now.month] + str(now.year) + ' ' + str(now.hour) + ':' + str(now.minute) + ':' + str(now.second) + """ UTC-3            
Server: MyServer/1.0 (Debian)\r\n\r\n""" + arquivo_string + corpo
            print('Arquivo '+palavras[1]+' encontrado.\n')
            print('Corpo requisição POST: '+ corpo + '\n')
            arquivo.close()

    except FileNotFoundError:
        print('Arquivo não encontrado.\n')
        response = """HTTP/1.1 404 File Not Found
Connection: close
Date: """ + days[now.weekday()] + str(now.day) + ' ' + months[now.month] + str(now.year) + ' ' + str(now.hour) + ':' + str(now.minute) + ':' + str(now.second) + """ UTC-3            
Server: MyServer/1.0 (Debian)"""

    except:
        print('Requisição inválida.\n')
        response = """HTTP/1.1 500 Bad Request
Connection: close
Date: """ + days[now.weekday()] + str(now.day) + ' ' + months[now.month] + str(now.year) + ' ' + str(now.hour) + ':' + str(now.minute) + ':' + str(now.second) + """ UTC-3            
Server: MyServer/1.0 (Debian)
            
"""     

    return str.encode(response)

def FTPresponse(receivedMessage, i):

    # o cliente pode apenas permanecer em Arquivos_server
    path = './Arquivos_server/'

    print(receivedMessage)

    if receivedMessage == 'QUIT':
        print("Achei um quit")
        return str.encode('Quiting'), 1
    else:
        receivedMessage = receivedMessage.split()
        comando = receivedMessage[0]

    # RETR {PATH/ARQUIVO_REMOTO}
    if comando == 'RETR':
        path += receivedMessage[1]
        if '..' in path:
            print('Acces denied for:'+ path + '\n')
            response = '550 Acces denied\r\n'
        else:
            data_socket = meu_socket("127.0.0.1", 19000 + i, "TCP")
            try:
                arquivo = open(path,'rb')
                data_socket.send_file(arquivo)
                response = '200 OK\r\n'
                print("File found")
            except:
                arquivo = open('./Arquivos_server/erro.txt', 'rb')
                data_socket.send_file(arquivo)
                response = '550 File Not Found\r\n'
                print("No such file")
            data_socket.close()
            
    else:
        response = "Not known method"
    return str.encode(response), 0
    


        
