import os
from confluent_kafka import Consumer

KAFKA_BROKER_URL = os.environ.get('KAFKA_BROKER_URL')
consumer = Consumer({
    'bootstrap.servers': KAFKA_BROKER_URL,
    'group.id': 'covid_cases_01',
    'auto.offset.reset': 'earliest'
})

consumer.subscribe(['global_covid_cases'])

while True:
  message = consumer.poll(1.0)

  if message is None:
      continue
  if message.error():
      print("Consumer error: {}".format(message.error()))
      continue

  print('Received message: {}'.format(message.value().decode('utf-8')))

consumer.close()
