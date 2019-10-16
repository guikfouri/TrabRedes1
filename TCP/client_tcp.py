from socket import *
serverName = '127.0.0.1'
serverPort = 17000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
sentence = input('Input lowercase sentece:')
#passar frase p/bytes
code = str.encode(sentence) 
clientSocket.send(code) 
modifiedSentence = clientSocket.recv(2048)
#passar frase p/string
modifiedSentence = modifiedSentence.decode()
print('From server:', modifiedSentence)
clientSocket.close()