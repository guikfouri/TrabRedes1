from TCPsocket import meu_socket
import sys
if __name__ == "__main__":
    client = meu_socket("127.0.0.1", 17000, "TCP")    
    # met = input('MÉTODO:\n')
    # url = input('ARQUIVO:\n')
    met = sys.argv[1]
    url = sys.argv[2]
    requisicao = met.upper() + ' /' + url + ' ' + 'HTTP/1.1'
    response = client.send_message(str.encode(requisicao))
    if response != '0':
        path = './Arquivos_client/' + url
        arq = open(path, 'w')
        arq.writelines(response)
        arq.close()
