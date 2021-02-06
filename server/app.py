from flask import Flask, jsonify, request
import pika
import json


app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def add():
    recv = request.json.get("r")
    cmd = request.json.get("c")
    values = {"r": recv, "c": cmd}
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq'))
    channel = connection.channel()
    channel.queue_declare(queue='task_queue', durable=True)
    channel.basic_publish(
        exchange='',
        routing_key='task_queue',
        body=json.dumps(values),
        properties=pika.BasicProperties(
            delivery_mode=2,  # make message persistent
        ))
    connection.close()
    return jsonify({"message": f"sent {cmd}"})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

