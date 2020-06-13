import socket

HEADERSIZE = 10

def CreateClientSocket():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #s.connect((socket.gethostname(), 1243))
    s.connect(('192.168.1.110', 5555))
    return s

def RunClientLoop(clientSocket):
    while True:
        full_msg = ''
        new_msg = True
        while True:
            msg = clientSocket.recv(16)
            if new_msg:
                msglen = int(msg[:HEADERSIZE])
                print("new msg len: " + str(msglen))
                new_msg = False

            full_msg += msg.decode("utf-8")

            print("Received bytes: " + str(len(full_msg)))

            if len(full_msg) - HEADERSIZE == msglen:
                print("full msg: " + full_msg)
                #print(full_msg[HEADERSIZE:])
                new_msg = True
                full_msg = ""


clientSocket = CreateClientSocket()
RunClientLoop(clientSocket)