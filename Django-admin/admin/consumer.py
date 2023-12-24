import pika

params = pika.URLParameters('amqps://zcsoshuo:xfEIqsjSocv3c0nbUaoFqBx6jwZpQFq2@albatross.rmq.cloudamqp.com/zcsoshuo')

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='admin')

def callback(ch, method, properties, body):
    print('receive in admin')
    print(body)

channel.basic_consume(queue='admin', on_message_callback=callback, auto_ack=True)

print('Started Consuming')

channel.start_consuming()

channel.close()