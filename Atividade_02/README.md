# Repositório para a atividade 2 de Sistemas distribuidos 2023.1

## Objetivo
Desenvolver uma aplicação simples de IoT para simular a detecção de incêndio em um ambiente, utilizando a temperatura da CPU como referência.

## Como rodar a aplicação:

### Requisitos:
* Maquina com o python 3.1X (versão usada no teste ou superior);
* Para uma melhor experiencia com a aplicação recomendamos que seja usada uma maquina com uma distribuição Linux.

### Instalações nescessarias

#### Instalar o RabbitMq Server

```bash
    sudo apt-get install rabbitmq-server
```
Atenção para instalar esse servidor precisará da sua senha

#### Instalar a blibioteca Pika do python com o comando

```bash
    pip install pika
```

#### Instalar a blibioteca Psutil do python com o comando

```bash
    pip install psutil
```

### Execute os sequintes comandos na pasta que estão os arquivos

#### Primeiro rode o arquivo do Produtor com 

```bash
    python3 producer.py
```

#### Abra outro terminal e execute o arquivo do consumidor

```bash
    python3 consumer.py
```

#### Abra outro terminal e execute o arquivo do alarme de incendio 

```bash
    python3 fire_alarm.py
```