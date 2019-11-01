from TCPsocket import meu_socket
import sys
if __name__ == "__main__":
    client = meu_socket("127.0.0.1", 17000, "TCP")    

    # método 'argv' recebe parâmetros separados por espaço
    met = sys.argv[1]
    arq = sys.argv[2]   

    response = client.send_message(str.encode(met + ' ' + arq))  # encode transforma os dados para bytes
    if response != '0':
        print('RESPOSTA FTP: response\n' + response)
        
