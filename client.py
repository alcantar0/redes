import socket
import random
from time import sleep


MIN = 10**9
MAX = 10**29

HOST = socket.gethostname();
PORT = 5000

def send_receive():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, 1234))

    random_value = random.randint(MIN, MAX)
    print(random_value.__sizeof__())
    client.sendall(str.encode(str(random_value)))

    msg = client.recv(90)
    print(msg.decode("utf-8"))


while True:
    send_receive()
    sleep(10)