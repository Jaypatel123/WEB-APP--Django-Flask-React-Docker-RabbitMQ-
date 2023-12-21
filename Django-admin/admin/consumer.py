import pika

params = pika.URLParameters('amqps://kshckzax:7u7qKSnPerZ3f748qARH6DDfDRav8eCg@beaver.rmq.cloudamqp.com/kshckzax')

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='admin')

def callback(ch, method, properties, body):
    print('Receive in admin')
    print(body)

channel.basic_consume(queue='admin', on_message_callback=callback)

print('Started Consuming')

channel.start_consuming()

channel.close()