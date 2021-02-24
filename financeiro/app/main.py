import pika
import time
from app.database import Database as db
import json

sleepTime = 10
print(' [*] Sleeping for ', sleepTime, ' seconds.')
time.sleep(30)

print(' [*] Connecting to server ...')
# register a RabbitMQ message
credentials = pika.PlainCredentials('guest', 'guest')
parameters = pika.ConnectionParameters('localhost', 5672, '/', credentials)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()
channel.queue_declare(queue='finalcial_queue', durable=True)

print(' [*] Waiting for messages.')

def callback(ch, method, properties, body):
  print(" [x] Received %s" % body)
  payload = json.loads(body.decode())
  print(" [x] Saving financial entry in the database")
  db.inicialize()
  db.save(payload)
  print(" [x] Done")
  ch.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='financial_queue', on_message_callback=callback)
channel.start_consuming()