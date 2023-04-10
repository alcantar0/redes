import socket 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1234))

s.sendall(str.encode("Ash nazg durbatulûk, ash nazg gimbatul, ash nazg thrakatulûk agh burzum-ishi krimpatul."))
msg = s.recv(1024) 
print(msg.decode("utf-8"))
