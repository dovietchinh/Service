import os 
from confluent_kafka import Producer,Consumer,TopicPartition
from confluent_kafka.admin import AdminClient,NewTopic
import threading
import traceback
class MyKafkaClient():

    def __init__(self,broker=None):
        if broker is None:
            broker = "127.0.0.1:9091,127.0.0.1:9092,127.0.0.1:9093"
            # broker = "localgh:10091"
        self.broker = broker
        conf = {
            'bootstrap.servers': self.broker,
            'group.id': 'mygroup',
            'session.timeout.ms': 6000,
            'auto.offset.reset': 'earliest',
            'security.protocol': 'PLAINTEXT',

        }
        self.admin_client = AdminClient(conf)
        self.producer = Producer(conf)
        self.consumer = Consumer(conf)
    
    def get_topics(self) -> dict:
        """
        Lists all topics.

        Returns:
        dict: A dictionary of topic names to TopicMetadata objects.
        """
        return self.producer.list_topics().topics

    def create_topic(self, topic_name,num_partitions=1, replication_factor=1) -> None:
        """
        Creates a Kafka topic.

        Parameters:
        topic_name (str): The name of the topic to create.

        Returns:
        None
        """
        new_topics = [NewTopic(topic=topic_name, num_partitions=num_partitions, replication_factor=replication_factor)]
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
            messages = self.consumer.consume(num_messages=1, timeout=1.0)
            if len(messages) == 0:
                continue 
            for message in messages:
                print('Received message: {}'.format(message.value().decode('utf-8')))

    def produce_message(self, topic_name: str, message: str) -> None:
        r = self.producer.produce(topic_name, message)
        print(f"Produced message: {type(r)}")

if __name__ == "__main__":
    kafka_client = MyKafkaClient()
    # print("[INFO]: ",f"all topics: ")
    # all_topics = kafka_client.get_topics()
    # for i in all_topics:
    #     print("[INFO]: topic: ",type(i))
    # kafka_client.create_topic("test")
    # kafka_client.delete_topic("test")

    # t = threading.Thread(target=kafka_client.consume_message, args=('test',))
    # t.start()
    # while True:
    #     message = input("Enter message: ")
    #     kafka_client.produce_message("test", message)
    #     time.sleep(1)
    choice = None
    try:
        while True:
            os.system('clear')
            print('MENU: ')
            print('1. Create topic')
            print('2. Delete topic')
            print('3. Consume_message')
            print('4. Write topic')
            print('5. Exit')
            print('6. List topics')
            print('7. Start consumer thread')
            if choice == '1':
                topic = input('Enter topic name: ')
                num_partitions = int(input('Enter number of partitions: '))
                replication_factor = int(input('Enter replication factor: '))
                kafka_client.create_topic(topic, num_partitions, replication_factor)
            elif choice == '2':
                topic = input('Enter topic name: ')
                kafka_client.delete_topic(topic)
            elif choice == '3':
                topic = input('Enter topic name: ')
                kafka_client.consume_message(topic)
            elif choice == '4':
                topic = input('Enter topic name: ')
                message = input('Enter message: ')
                kafka_client.produce_message(topic, message)
            elif choice == '5':
                break
            elif choice == '6':
                print(kafka_client.get_topics())
            else:
                # print('Invalid choice')
                pass
            choice = input('Enter choice: ')
    except Exception as e:
        traceback.print_exc()
        print('Exiting...')
        exit(0)
