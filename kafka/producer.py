import base64
from kafka import KafkaProducer
from kafka.errors import KafkaError
image = open('bird-thumbnail.jpg', 'rb')
image_read = image.read()
image_64_encode = base64.b64encode(image_read)
producer= KafkaProducer(bootstrap_servers ='localhost:9092')
future = producer.send('topic-01', image_64_encode)
try:
    record_metadata = future.get(timeout=10)
except KafkaError:
    log.exception()
    pass