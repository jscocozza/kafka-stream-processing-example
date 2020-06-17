import json
import os
import requests
import time

from confluent_kafka import Producer

def delivery_report(err, msg):
    """ Called once for each message produced to indicate delivery result.
        Triggered by poll() or flush(). """
    if err is not None:
        print('Message delivery failed: {}'.format(err))
    else:
        print('Message delivered to {} [{}]'.format(msg.topic(), msg.partition()))


KAFKA_BROKER_URL = os.environ.get('KAFKA_BROKER_URL')
GLOBAL_COVID_19_URL = "https://thevirustracker.com/free-api?global=stats"

producer = Producer({'bootstrap.servers': KAFKA_BROKER_URL})

while True:
    # Trigger any available delivery report callbacks from previous produce() calls
    producer.poll(0)

    response = requests.get(url=GLOBAL_COVID_19_URL)
    global_covid_data = json.loads(response.text)["results"][0]
    
    producer.produce(
      'global_covid_cases',
      json.dumps(global_covid_data),
      callback=delivery_report
    )

    # Wait for any outstanding messages to be delivered and delivery report
    # callbacks to be triggered.
    producer.flush()

    # Wait 5 seconds before sending another requests
    time.sleep(5)
