from TCPsocket import meu_socket
import sys
if __name__ == "__main__":
    client = meu_socket("127.0.0.1", 17000, "TCP")    

    # método 'argv' recebe parâmetros separados por espaço
    met = sys.argv[1]
    url = sys.argv[2]   

    if met == 'GET':
        requisicao = met.upper() + ' /' + url + ' ' + 'HTTP/1.1'
    elif met == 'POST':
        requisicao = met.upper() + ' /' + url + ' ' + 'HTTP/1.1' + '\r\n\r\n' + sys.argv[3]

    response = client.send_message(str.encode(requisicao))  # encode transforma os dados para bytes
    if response[9:13] == '200':
        path = './Arquivos_client/' + url
        arq = open(path, 'w')
        arq.writelines(response)
        arq.close()
    client.close()

        print("\tMensagem de resposta obtida\r\n\r\n" + response)
    
