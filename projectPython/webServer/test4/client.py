import socket


class Client:
    def __init__(self,ClientMessage):
        self.target_host = 'localhost'
        self.target_port = 9998
        self.ClientMessage=bytes(ClientMessage,'utf-8')

    def runClient(self):
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((self.target_host,self.target_port))

        client.send(self.ClientMessage)

        responseToClient = client.recv(4096)
        print(responseToClient.decode())
        client.close()


if __name__=='__main__':
    while True:
        ClientSmS = input("[+]Input data you want to send >:")
        ClientConnector = Client(ClientSmS)
        ClientConnector.runClient()