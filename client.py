import socket
import random
from time import sleep

MIN = 10**9
MAX = 10**30
RESPONSE_SIZE = 10**2

HOST = socket.gethostname();
PORT = 1234

def send_receive():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))

    random_value = str(random.randint(MIN, MAX))
    client.sendall(str.encode(random_value))

    msg = client.recv(RESPONSE_SIZE)
    print(msg.decode("utf-8") + " FIM")


while True:
    send_receive()
    sleep(10)