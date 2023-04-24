import socket
from time import sleep
from random import choice

RESPONSE_SIZE = 10**2
HOST = socket.gethostname()
PORT = 1234

def send_to_server():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))

    numbers = [121213,88754,4*10**11,3*10**29]
    random_value = str(choice(numbers))
    client.sendall(str.encode(random_value))
    msg = client.recv(RESPONSE_SIZE)

    print("Number of Digits:", len(random_value) , "," +
          "Number: " + random_value + ", " +
          "Result: " + msg.decode("utf-8") + " FIM")

while True:
    send_to_server()
    sleep(10)