import socket
import string
import random

RESPONSE_SIZE = 10**2

HOST = socket.gethostname();
PORT = 5000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((socket.gethostname(), 1234))
server.listen()

def random_string(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))

while True:
    clientsocket, address = server.accept()
    print(f"Connection from {address} has been established!")

    client_data = clientsocket.recv(RESPONSE_SIZE)
    received_number = (client_data.decode())

    received_lenght = len(received_number)
    if received_lenght > 10:
        generated_string = random_string(received_lenght)
        clientsocket.sendall(str.encode(generated_string))
    else:
        if received_number % 2 == 0:
            clientsocket.sendall("PAR".encode())
        else:
            clientsocket.sendall("IMPAR".encode())

clientsocket.close()
s.close()
