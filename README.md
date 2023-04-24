# Trabalho da disciplina de Redes de Computadores - 2023.1

## O código está dividido em dois arquivos: client.py e server.py

## *client.py*
Nesse arquivo está a funcão _send_to_server()_ onde através da biblioteca socket é possível criar um socket TCP:
Há três variáveis globais: RESPONSE_SIZE, que é o tamanho do buffer para o recebimento da mensagem do servidor;
HOST, que utiliza a função socket.gethostname(); e PORT, que define a porta padrão.
```python
RESPONSE_SIZE = 10**2
HOST = socket.gethostname()
PORT = 1234
```

```python
# _socket.SOCK_STREAM_ define o protocolo TCP.
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
```
Para facilitar os testes durante o desenvolvimento, é utilizado um vetor de numeros pré-estabelecidos, assim a função random possui um escopo menor de números e possível visualizar quando o número tem menos ou mais de 10 casas.
```python
numbers = [121213,88754,4*10**11,3*10**29]
random_value = str(choice(numbers))
```
Fora da função, a um laço _while_ que chama a função _send_to_server_ e espera por 10 segundos.
```python
while True:
    send_to_server()
    sleep(10)
```

## *server.py*

Até a décima sexta linha é o mesmo procedimento de configuração do socket TCP e as variáveis globais explicadas no arquivo anterior.
Existe a função _random_string_ que recebe o número de casas do número(_length_). Na função é definida as letras minúsculas e retorna uma string aleatória tomando-as como base.
```python
def random_string(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))
```
Fora dessa função, no escopo principal do código, existe um laço _while_ que irá lidar com as requisições do cliente.
```python
#Servidor aceitar conexão, recebe a mensagem e a decodifica.
clientsocket, address = server.accept()
client_data = clientsocket.recv(RESPONSE_SIZE)
received_number = (client_data.decode())
```

O restante do códigodentro do laço irá verificar se quantidade de casas do número recebido pelo cliente é menor ou maior que 10. Se for maior, a função _random_string_ será chamada e será passado o número de casas do número como parâmetro.
```python
#Número de casas do número.
received_lenght = len(received_number)
```
```python
if received_lenght > 10:
    generated_string = random_string(received_lenght)
```
```python
# E é mandada a string aleatória com _received_length_ de tamanho.
clientsocket.sendall(str.encode(generated_string))
```
Caso o número tenhas menos que 10 casas, irá verificar se o número é par ou impar e mostrará o resultado no terminal.
```python
    else:
        if int(received_number) % 2 == 0:
            clientsocket.sendall("PAR".encode())
        else:
            clientsocket.sendall("IMPAR".encode())
```
É importante perceber que o código na linha 12 serve para que após a execução do server.py seja interrompida, não aconteça a espera por conta do erro «Address already in use» («_Endereço já está em uso_»).
```python
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
```
E por fim o é fechado o _socket_ dentro do laço:
```python
clientsocket.close()
```
