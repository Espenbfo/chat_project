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
        print(model.parse(bytes.decode(body)))
        print(f"finished parsing in {time.time() - st} seconds")
    else:
        print('No message returned')