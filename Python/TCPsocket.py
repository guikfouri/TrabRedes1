from socket import *

#requisição: {METODO} {URI} HTTP/{VERSAO}\r\n
#\r\n
#{DADOS}

#resposta: HTTP/{VERSAO} {CODIGO}\r\n
#\r\n
#{DADOS}


# recebe uma requisição HTTP em bytes ou str
# e retorna uma resposta HTTP em str
def HTTPresponse(receivedMessage):
    if type(receivedMessage) == 'bytes':
        requisicao = receivedMessage.decode()
    else:
        requisicao = receivedMessage
    print('Requisição HTTP:'+requisicao)

    requisicao = requisicao.split()
    try:
        if requisicao[0] == 'GET':
            path = '../Arquivos_teste' + requisicao[1]
            arquivo = open(path,'r')
            print('Arquivo '+requisicao[1]+' encontrado.\n')

            dados = ''
            for linha in arquivo:
                dados += linha
            codigo = '200 OK'

            arquivo.close()

    except:
        print('Arquivo não encontrado.\n')
        dados = ''
        codigo = '404 Not Found'
        #melhorar mensagem resposta de erro com cabeçalho HTTP
    resposta = r'HTTP/1.1 {}\r\n\r\n{}'.format(codigo, dados)
    return resposta


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

            if self.protocol == "HTTP" :
                responseMessage = HTTPresponse(receivedMessage)
            elif self.protocol == "FTP" :
                responseMessage = FTPresponse(receivedMessage)

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
            
            resposta = HTTPresponse(receivedMessage)
            connectionSocket.send(str.encode(resposta))
            connectionSocket.close()

            # try:
            #     if requisicao[0] == 'GET':
            #         path = '../Arquivos_teste/' + requisicao[1]
            #         arquivo = open(path,'rb')
            #         connectionSocket.sendfile(arquivo)
            #         print('Arquivo '+requisicao[1]+' encontrado.\n')
            #     arquivo.close()

            # except FileNotFoundError:
            #     print('Arquivo não encontrado.\n')
            #     erro = 'ERRO 404'
            #     #melhorar mensagem resposta de erro com cabeçalho HTTP

            #     connectionSocket.send(str.encode(erro))

            # except:
            #     print('Requisição inválida.\n')

            #responseMessage = HTTPresponse(receivedMessage) 
            #connectionSocket.send(responseMessage)
            
                
                

    


        
