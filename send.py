import pika
from pika import channel

queue_name = 'test-queue'

conn = pika.BlockingConnection(pika.ConnectionParameters('127.0.0.1'))
channel = conn.channel()

channel.queue_declare(queue_name)

for i in range(1, 10000):
    channel.basic_publish(exchange='', routing_key=queue_name, body='message: ' + str(i))
    print('message: ' + str(i))


conn.close()
