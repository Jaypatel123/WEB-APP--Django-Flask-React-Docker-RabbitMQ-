import pika

params = pika.URLParameters('amqps://kshckzax:7u7qKSnPerZ3f748qARH6DDfDRav8eCg@beaver.rmq.cloudamqp.com/kshckzax')

connection = pika.BlockingConnection(params)

channel = connection.channel()

def publish():
    channel.basic_publish(exchange="", routing_key='admin', body='hello')