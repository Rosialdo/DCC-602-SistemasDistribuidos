import pika
import psutil
import time

# Estabelecendo uma conexão com o servidor RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

# Criando um canal de comunicação
channel = connection.channel()

# Declarando a fila que será usada
channel.queue_declare(queue='temperature')


def publish_temp_cpu():
    # Obtendo a temperatura da CPU usando o módulo psutil
    temperature = psutil.sensors_temperatures()['coretemp'][0].current

    # Publicando a temperatura na fila 'temperature'
    channel.basic_publish(exchange='', routing_key='temperature', body=str(temperature))


while True:
    # Chamando a função para publicar a temperatura da CPU
    publish_temp_cpu()

    # Aguardando 5 segundos antes de chamar a função novamente
    time.sleep(5)
