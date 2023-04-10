import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1234))
s.listen()

while True:
    clientsocket, address = s.accept()
    print(f"Connection from {address} has been established!")
    clientsocket.send(bytes("Welcome to the Server", "utf-8"))
    data = clientsocket.recv(1024)
    if not data:
        print("bye")
        clientsocket.close()
    print(data.decode())
    clientsocket.sendall(data)


