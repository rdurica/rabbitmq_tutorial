import pika
from pika import channel
import os
import sys

queue_name = 'test-queue'


def receiver():
    conn = pika.BlockingConnection(parameters=pika.ConnectionParameters('127.0.0.1'))
    channel = conn.channel()

    channel.queue_declare(queue=queue_name)

    def callback(ch, method, properties, body):
        print(f'Received --- {body}')

    channel.basic_consume(queue=queue_name,
                          auto_ack=True,
                          on_message_callback=callback)

    print('Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()


if __name__ == '__main__':
    try:
        receiver()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
