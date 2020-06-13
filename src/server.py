import socket
import time

HEADERSIZE = 10

def SendString(clientsocket, msg):
    msg = f"{len(msg):<{HEADERSIZE}}"+msg
    print("Sending: " + msg)
    clientsocket.send(bytes(msg,"utf-8"))

def CreateSocket():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('0.0.0.0', 5555))
    s.listen(5)
    return s

def RunServerLoop(serverSocket):
    # now our endpoint knows about the OTHER endpoint.
    clientsocket, address = serverSocket.accept()
    print(f"Connection from {address} has been established.")

    SendString(clientsocket, "Welcome to the server!")

    while True:
        time.sleep(3)
        SendString(clientsocket, f"The time is {time.time()}0")


serverSocket = CreateSocket()
RunServerLoop(serverSocket)