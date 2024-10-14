import os 
from confluent_kafka import Producer,Consumer,TopicPartition
from confluent_kafka.admin import AdminClient,NewTopic
import threading
class MyKafkaClient():

    def __init__(self,broker=None):
        if broker is None:
            broker = "localhost:9092"
        self.broker = broker
        self.admin_client = AdminClient({
            'bootstrap.servers': self.broker
        })
        self.producer = Producer({
            'bootstrap.servers': self.broker
        })

        self.consumer = Consumer({
            'bootstrap.servers': self.broker,
            'group.id': 'mygroup',
        })
    
    def get_topics(self) -> dict:
        """
        Lists all topics.

        Returns:
        dict: A dictionary of topic names to TopicMetadata objects.
        """
        return self.consumer.list_topics().topics

    def create_topic(self, topic_name):
        """
        Creates a Kafka topic.

        Parameters:
        topic_name (str): The name of the topic to create.

        Returns:
        None
        """
        new_topics = [NewTopic(topic=topic_name, num_partitions=1, replication_factor=1)]
        fs = self.admin_client.create_topics(new_topics)
        for topic, f in fs.items():
            try:
                f.result()  # The result itself is None
                print(f"Topic {topic} created")
            except Exception as e:
                print(f"Failed to create topic {topic}: {e}")

    def delete_topic(self, topic_name: str) -> None:
        result = self.admin_client.delete_topics([topic_name])  # return future object
        for k, v in result.items():
            try:
                v.result()
                print(f"Topic {k} deleted")
            except Exception as e:
                print(f"Failed to delete topic {k}: {e}")

    def consume_message(self, topic_name: str) -> None:
        self.consumer.subscribe([topic_name])
        while True:
            message = self.consumer.poll()
            if message is None:
                continue
            if message.error():
                print("Consumer error: {}".format(message.error()))
                continue
            print('Received message: {}'.format(message.value().decode('utf-8')))

    def read_topic(self,topic):
        self.consumer.subscribe([topic])
        while True:
            message = self.consumer.poll()
            if message is None:
                continue
            if message.error():
                print("Consumer error: {}".format(message.error()))
                continue
            print('Received message: {}'.format(message.value().decode('utf-8')))

    def produce_message(self, topic_name: str, message: str) -> None:
        r = self.producer.produce(topic_name, message)
        print(f"Produced message: {type(r)}")

    def start_consumer_thread(self, topic_name: str) -> None:
        t = threading.Thread(target=self.consume_message, args=(topic_name,))
        t.start()

if __name__ == "__main__":
    kafka_client = MyKafkaClient()
    print("[INFO]: ",f"all topics: ")
    all_topics = kafka_client.get_topics()
    for i in all_topics:
        print("[INFO]: topic: ",type(i))
    kafka_client.create_topic("test")
    kafka_client.delete_topic("test")

    t = threading.Thread(target=kafka_client.consume_message, args=('test',))
    t.start()
    while True:
        message = input("Enter message: ")
        kafka_client.produce_message("test", message)
        time.sleep(1)

