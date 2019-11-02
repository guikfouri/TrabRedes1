from TCPsocket import meu_socket
import sys

if __name__ == "__main__":
    client = meu_socket("127.0.0.1", 18000, "TCP")    

    # método 'argv' recebe parâmetros separados por espaço
    message = input("Requisição FTP:\n")
    met = message.split()
    while(message[0:4] == "QUIT"):

        response = client.send_message(str.encode(message))  # encode transforma os dados para bytes

        if met[0] == 'RETR':
            data_socket = meu_socket("127.0.0.1", 19000, "TCP")
            data_socket.receiveData()

        elif met[0] == 'STOR':
            data_socket = meu_socket("127.0.0.1", 19000, "TCP")


        print('RESPOSTA FTP:\n' + response)

        message = input("Requisição FTP:\n")
        
