import pika

# Estabelecendo uma conexão com o servidor RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

# Criando um canal de comunicação
channel = connection.channel()

# Declarando as filas que serão usadas
channel.queue_declare(queue='temperature')
channel.queue_declare(queue='fire_alert')


def callback(ch, method, properties, body):
    # Função de retorno chamada quando uma mensagem é recebida

    # Convertendo o corpo da mensagem em um valor numérico de ponto flutuante
    temperature = float(body)

    if temperature > 51:
        # Se a temperatura for maior que 51, publica uma mensagem na fila 'fire_alert'
        channel.basic_publish(exchange='', routing_key='fire_alert', body='FIRE DETECTED!')
        print('Incêndio detectado! Temperatura:', temperature)
    else:
        # Caso contrário, imprime a temperatura normalmente
        print('Temperatura:', temperature)


# Configurando o consumo da fila 'temperature' e especificando a função de retorno
channel.basic_consume(queue='temperature', on_message_callback=callback, auto_ack=True)

print('Aguardando...')
# Iniciando o consumo das mensagens
channel.start_consuming()
