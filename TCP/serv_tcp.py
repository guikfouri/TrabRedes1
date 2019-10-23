from socket import *
serverPort = 17000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)

print('The server is ready to receive')
while 1:
    connectionSocket, addr = serverSocket.accept()
    requisicao = connectionSocket.recv(2048)
    requisicao = requisicao.decode()
    print(requisicao)
    try:
        lista = requisicao.split()
        if lista[0] == 'GET':
            arquivo = open(lista[1], 'rb')
            #falta colocar o cabecalho na resposta
            #cabecalho = 'HTTP/1.1 200 Ok\n\r\n\r'
            #connectionSocket.send(cabecalho)
            connectionSocket.sendfile(arquivo)
        arquivo.close()
    
    except:
        print('Arquivo não encontrado')
        erro = 'ERROR 404'
        erro = str.encode(erro)
        connectionSocket.send(erro)
    connectionSocket.close()

# arquivo.seek(0, 2)
# tamanho = arquivo.tell()    
# arquivo.seek(0)
# buffer = arquivo.read(tamanho)
















# from socket import *
# serverPort = 12000
# serverSocket =socket(AF_INET, SOCK_STREAM)
# serverSocket.bind(('', serverPort))
# serverSocket.listen(1)
# print('The server is ready to receive')
# while 1:
#     connectionSocket, addr = serverSocket.accept()
#     requisicao = connectionSocket.recv(2048)

#     capitalizedrequisicao = requisicao.upper()
#     connectionSocket.send(capitalizedrequisicao)
#     connectionSocket.close()
