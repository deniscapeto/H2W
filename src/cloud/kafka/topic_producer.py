import json

from kafka import KafkaProducer

producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)
topic = 'teste_kefka_python'

future = producer.send(topic, {'foo': 'bar'})
ret = future.get(timeout=30)

print(ret.topic)
print(ret.partition)
print(ret.offset)

producer.flush()
producer.close()
