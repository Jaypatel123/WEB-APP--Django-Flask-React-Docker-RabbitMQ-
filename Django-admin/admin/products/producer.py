import pika, json

params = pika.URLParameters('amqps://kshckzax:7u7qKSnPerZ3f748qARH6DDfDRav8eCg@beaver.rmq.cloudamqp.com/kshckzax')

connection = pika.BlockingConnection(params)

channel = connection.channel()

def publish(method, body): # creating a publish trigger whenever product is interacted
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange="", routing_key='main', body=json.dumps(body), properties=properties)