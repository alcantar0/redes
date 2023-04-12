import socket as network
from time import sleep
from random import randint as gerador_numero

MAX = 10**30
RESPONSE_SIZE = 10**2
HOST = network.gethostname();
PORT = 1234

def send_to_server():
    client = network.socket(network.AF_INET, network.SOCK_STREAM)
    client.connect((HOST, PORT))

    random_value = str(gerador_numero(0, 10**30))
    client.sendall(str.encode(random_value))

    msg = client.recv(RESPONSE_SIZE)
    print(msg.decode("utf-8") + " FIM")

while True:
    send_to_server()
    sleep(10)