# Repositório para a atividade 4 de Sistemas distribuidos 2023.1

## Objetivo

Modificar o exemplo de cliente e servidor gRPC visto anteriormente para criar uma aplicação de controle remoto de uma máquina Linux. O objetivo é permitir que o cliente envie comandos em formato de string para o servidor, que irá executar esses comandos em uma máquina Linux e retornar o resultado para o cliente.

## Descrição

A aplicação deverá ser composta por um servidor e um cliente, implementados usando gRPC e Python. O servidor deve estar configurado para receber comandos em formato de string do cliente e executá-los em uma máquina Linux. O cliente deve permitir que o usuário insira os comandos que deseja executar e exibir o resultado da execução.

## Como rodar a aplicação:

### Requisitos:
* Maquina com o python 3.1X.X (versão usada no teste ou superior)

### verifique se você tem o grpcio e o grpcio-tools instalados em sua máquina.

```bash
 pip install grpcio grpcio-tools
```

### também é necessário instalar a lib click

```bash
 pip install click
```

### Precaução 
Certifique-se de salvar o arquivo remote_control.proto, server.py e client.py na mesma pasta. <br></br>

### Em seguida, você pode gerar os arquivos Python necessários para o gRPC executando o seguinte comando: 

``` bash
python3 -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. remote_control.proto
```

### para iniciar o servidor, execute o seguinte comando:

```bash
python3 server.py
```

### para iniciar o cliente, execute o seguinte comando:

```bash
python3 client.py
```

<span style="color: red;">É importante que o servidor seja o primeiro a ser execultado caso contrario o programa não vai ser rodado de forma correta</span>


