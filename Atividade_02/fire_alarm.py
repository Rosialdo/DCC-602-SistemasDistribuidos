import pika

# Estabelecendo uma conexão com o servidor RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

# Criando um canal de comunicação
channel = connection.channel()

# Declarando a fila que será usada
channel.queue_declare(queue='fire_alert')


def callback(ch, method, properties, body):
    # Função de retorno chamada quando uma mensagem é recebida

    # Imprimindo mensagem de "Fogo Detectado!"
    print('Fogo Detectado!')

    # Publicando uma mensagem na fila 'fire_prevention_system'
    channel.basic_publish(exchange='', routing_key='fire_prevention_system', body='Ativar sistema de prevenção de incêndio')

    # Imprimindo mensagem de "Sistema de alarme de incêndio ativado"
    print('Sistema de alarme de incêndio ativado')


# Configurando o consumo da fila 'fire_alert' e especificando a função de retorno
channel.basic_consume(queue='fire_alert', on_message_callback=callback, auto_ack=True)

# Iniciando o consumo das mensagens
channel.start_consuming()
