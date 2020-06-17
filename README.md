# Kafka Stream Processing Example
The Producer gets COVID-19 data every 5 seconds and sends the information into `global_covid_cases` topic with 3 partitions.
The Consumer is responsible for receiving the information from the mentioned topic.

### Setup
- `docker network create kafka-network`

In one terminal run: 
- `docker-compose -f docker-compose-kafka.yml up`

In another terminal run:
- `docker-compose up`
