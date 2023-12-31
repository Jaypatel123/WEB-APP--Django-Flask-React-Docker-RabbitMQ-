import pika, json

params = pika.URLParameters('amqps://zcsoshuo:xfEIqsjSocv3c0nbUaoFqBx6jwZpQFq2@albatross.rmq.cloudamqp.com/zcsoshuo')

connection = pika.BlockingConnection(params)

channel = connection.channel()

def publish(method, body): # creating a publish trigger whenever product is interacted
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange="", routing_key='admin', body=json.dumps(body), properties=properties)

# def publish(): # creating a publish trigger whenever product is interacted
#     channel.basic_publish(exchange="", routing_key='main', body='Hello Admin')