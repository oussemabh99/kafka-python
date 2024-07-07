from kafka import KafkaConsumer
import base64
consumer = KafkaConsumer('topic-01',bootstrap_servers=['localhost:9092'])
for message in consumer:
    print ("%s:%d:%d: key=%s " % (message.topic, message.partition,message.offset, message.key))
    value = message.value
    try:
       image_result = open(r'/home/hdid/kafka-python/images/image2.jpg', 'wb')
       image_64_decode = base64.b64decode(value)
       image_result.write(image_64_decode)
    except:
        print('error')                         