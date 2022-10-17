import pika
import sys

"""
See tutorial https://www.rabbitmq.com/tutorials/tutorial-two-python.html
"""

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='192.168.88.222'))
channel = connection.channel()

channel.queue_declare(queue='task_queue', durable=True)

message = ' '.join(sys.argv[1:]) or "Hello World!"
channel.basic_publish(
    exchange='',
    routing_key='task_queue',
    body=message,
    properties=pika.BasicProperties(
        delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE
    ))
print(" [x] Sent %r" % message)
connection.close()