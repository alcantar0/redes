import socket
from time import sleep
from random import (choice, randint as number_generator)

MAX = 10**29
RESPONSE_SIZE = 10**2
HOST = socket.gethostname()
PORT = 1234

def generate_number_by_lenght(min: int, max: int, size: int):
    return str(number_generator(min, max))[:size]

def generate_number():
    number = number_generator(1,99)
    less_or_equal_to_ten_digits = int(generate_number_by_lenght(0, 10**9, 10))
    greater_than_ten_digits = int(generate_number_by_lenght(10**10, MAX, 30))
    sizes = [less_or_equal_to_ten_digits, greater_than_ten_digits]
    return number * choice(sizes)

def send_to_server():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))

    random_value = str(generate_number())[:30]
    client.sendall(str.encode(random_value))
    msg = client.recv(RESPONSE_SIZE)

    print("Number of Digits:", len(random_value) , "," +
          "Number: " + random_value + ", " +
          "Result: " + msg.decode("utf-8") + " FIM")

while True:
    send_to_server()
    sleep(10)