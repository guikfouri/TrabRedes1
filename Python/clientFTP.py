from TCPsocket import meu_socket
import sys

i = 0

if __name__ == "__main__":
    client = meu_socket("127.0.0.1", 18000, "TCP")    
    client.connect()

    message = '      '

    while (message[0:4] != "QUIT"):

        message = input("Requisição FTP:\n")
        met = message.split()

        response = client.send_message(str.encode(message), i)  # encode transforma os dados para bytes
        i += 1
        if met[0] == 'STOR':
            path = './Arquivos_client/' + met[1]
            arq = open(path, 'r')
            data_socket.send_file(arq)

        print('RESPOSTA FTP:\n' + response)
            
    client.close()
        
