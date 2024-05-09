import pika
from envs import *
from dto import Student

def getPikaConnection():
    credentials = pika.PlainCredentials(RABBITMQ_USERNAME, RABBITMQ_PASSWORD)
    parameters = pika.ConnectionParameters(RABBITMQ_HOST, RABBITMQ_PORT, '/',  credentials)
    return pika.BlockingConnection(parameters)

def getConnection():
    parameters = pika.ConnectionParameters(RABBITMQ_HOST)
    return pika.BlockingConnection(parameters)

def publishMessage(message: Student):
    connection = getPikaConnection()
    channel = connection.channel()
    channel.queue_declare(queue=RABBITMQ_QUEUE, durable=True)
    channel.basic_publish(exchange=RABBITMQ_EXCHANGE, routing_key=RABBITMQ_ROUTING, body=message.model_dump_json())
    connection.close()

def listenMessage(function):
    connection = getConnection()
    channel = connection.channel()
    channel.queue_declare(queue=RABBITMQ_QUEUE, durable=True)

    def callback(ch, method, properties, body):
        function(body)

    channel.basic_consume(queue=RABBITMQ_QUEUE, on_message_callback=callback, auto_ack=True)
    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()
    connection.close()