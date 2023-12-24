import pika, json
from main import Product, db
from flask import Flask

app = Flask(__name__)

params = pika.URLParameters('amqps://zcsoshuo:xfEIqsjSocv3c0nbUaoFqBx6jwZpQFq2@albatross.rmq.cloudamqp.com/zcsoshuo')

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='main')

def callback(ch, method, properties, body):
    data = json.loads(body)
    print('recived messsage to main docker container')
    print(data)
    with app.app_context():
        if properties.content_type == 'product_created':
            product = Product(id=data['id'], title=data['title'], image=data['image'])
            print(product.id, product.title, product.image)
            db.session.add(product)
            db.session.commit()
            print('Product Created')        

        elif properties.content_type == 'product_updated':
            product = Product.query.get(data['id'])
            product.title = data['title']
            product.image = data['image']
            db.session.commit()
            print('Product Updated')

        elif properties.content_type == 'product_deleted':
            product = Product.query.get(data)
            db.session.delete(product)
            db.session.commit()
            print('Product Deleted')

channel.basic_consume(queue='main', on_message_callback=callback, auto_ack=True)


print('Started Consuming')

channel.start_consuming()

channel.close()