from TCPsocket import meu_socket

if __name__ == "__main__":
    client = meu_socket("127.0.0.1", 17000, "TCP")
    response = client.send_message(str.encode("C"))
    print(response)
