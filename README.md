# Trabalho da disciplina de Redes de Computadores, 2023.1

## O código está dividido em dois arquivos: client.py e server.py

## *client.py*:
Nesse arquivo está a funcão _send_to_server()_ onde através da biblioteca socket é possível criar um socket TCP:
Há três variáveis globais: RESPONSE_SIZE, que é o tamanho do buffer para o recebimento da mensagem do servidor;
HOST, que utiliza a função socket.gethostname(); e PORT, que define a porta padrão.
```bash
RESPONSE_SIZE = 10**2
HOST = socket.gethostname()
PORT = 1234
```

```bash
# _socket.SOCK_STREAM_ define o protocolo TCP.
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
```
Para facilitar os testes durante o desenvolvimento, é utilizado um vetor de numeros pré-estabelecidos, assim a função random possui um escopo menor de números e possível visualizar quando o número tem menos ou mais de 10 casas.
```bash
numbers = [121213,88754,4*10**11,3*10**29]
random_value = str(choice(numbers))
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
```
Fora da função, a um laço _while_ que chama a função _send_to_server_ e espera por 10 segundos.
```bash
while True:
    send_to_server()
    sleep(10)
```
