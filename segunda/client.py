import socket

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

client.sendto("Ash nazg durbatulûk, ash nazg gimbatul, ash nazg thrakatulûk agh burzum-ishi krimpatul.".encode('utf-8'), ("127.0.0.1", 9999))

print(client.recvfrom(1024)[0].decode('utf-8'))
