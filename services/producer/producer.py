import os
from confluent_kafka import Producer

KAFKA_BROKER_URL = os.environ.get('KAFKA_BROKER_URL')
producer = Producer({'bootstrap.servers': KAFKA_BROKER_URL})

def delivery_report(err, msg):
    """ Called once for each message produced to indicate delivery result.
        Triggered by poll() or flush(). """
    if err is not None:
        print('Message delivery failed: {}'.format(err))
    else:
        print('Message delivered to {} [{}]'.format(msg.topic(), msg.partition()))

for data in ["hola", "como va?", "chau"]:
    print("PRODUCING MESSAGES!")
    
    # Trigger any available delivery report callbacks from previous produce() calls
    producer.poll(0)

    # Asynchronously produce a message, the delivery report callback
    # will be triggered from poll() above, or flush() below, when the message has
    # been successfully delivered or failed permanently.
    producer.produce(
      'event_messages_topic',
      data.encode('utf-8'),
      callback=delivery_report
    )

# Wait for any outstanding messages to be delivered and delivery report
# callbacks to be triggered.
producer.flush()