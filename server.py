import socket as network
import string
import random

RESPONSE_SIZE = 10**2

HOST = network.gethostname();
PORT = 1234

server = network.socket(network.AF_INET, network.SOCK_STREAM)
server.bind((network.gethostname(), PORT))
server.listen()

def random_string(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))

while True:
    clientsocket, address = server.accept()
    client_data = clientsocket.recv(RESPONSE_SIZE)
    received_number = (client_data.decode())

    received_lenght = len(received_number)
    if received_lenght > 10:
        generated_string = random_string(received_lenght)
        clientsocket.sendall(str.encode(generated_string))
    else:
        if int(received_number) % 2 == 0:
            clientsocket.sendall("PAR".encode())
        else:
            clientsocket.sendall("IMPAR".encode())

clientsocket.close()
s.close()
