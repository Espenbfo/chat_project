import pika
import torch
from pika.channel import Channel

from voice_parser import WhisperModel
import time

print("gpu?", torch.cuda.is_available())
# Create a global channel variable to hold our channel object in

model = WhisperModel()

# Step #1: Connect to RabbitMQ using the default parameters
connection = pika.BlockingConnection()
channel = connection.channel()
channel.queue_delete(queue="test")
channel.queue_declare(queue="test")
while True:
    time.sleep(1)
    method_frame, header_frame, body = channel.basic_get('test')
    if method_frame:
        print(method_frame, header_frame, body)
        print("starting parsing")
        st = time.time()
        file_path, id = bytes.decode(body).split("|")
        text = model.parse(file_path)["text"]
        print(f"finished parsing in {time.time() - st} seconds")
        channel.basic_publish(exchange="", routing_key=id,body=bytes(text, "utf-8"))
    else:
        print('No message returned')