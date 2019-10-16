from socket import *
serverPort = 17000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print('The server is ready to receive')
while 1:
    connectionSocket, addr = serverSocket.accept()
    sentence = connectionSocket.recv(2048)
    sentence = sentence.decode()
    print(sentence)
    try:
        arquivo = open(sentence, 'rb')
        connectionSocket.sendfile(arquivo)
        arquivo.close()
    except:
        print('Arquivo não encontrado.')
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
#     sentence = connectionSocket.recv(2048)

#     capitalizedSentence = sentence.upper()
#     connectionSocket.send(capitalizedSentence)
#     connectionSocket.close()
