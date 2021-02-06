import pika
import time
import json
from mailer import send_mail


sleepTime = 10
print('[worker] Sleeping for ', sleepTime, ' seconds.')
time.sleep(sleepTime)

print('[worker] Connecting to server ...')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq'))
channel = connection.channel()
channel.queue_declare(queue='task_queue', durable=True)

print('[worker] Waiting for messages.')


def callback(ch, method, properties, body):
    print("[worker] Received %s" % body)
    values = json.loads(body)
    send_mail(values.get("c"), values.get("r"))
    print("[worker] Done")

    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='task_queue', on_message_callback=callback)
channel.start_consuming()

