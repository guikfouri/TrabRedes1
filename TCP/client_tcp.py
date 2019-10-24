from socket import *
serverName = '127.0.0.1'
serverPort = 17000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))

met = input('MÉTODO:\n')
url = input('ARQUIVO:\n')
sentence = met.upper() + ' ' + url + ' ' + 'HTTP/1.1'

#passar frase p/bytes
code = str.encode(sentence) 
clientSocket.send(code) 


#while(1):    
modifiedSentence = clientSocket.recv(2048)
#passar frase p/string
modifiedSentence = modifiedSentence.decode()
    



print(modifiedSentence)
clientSocket.close()