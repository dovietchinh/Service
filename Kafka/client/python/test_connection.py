import confluent_kafka

def test_connections():
    brokers = "localhost:9092"
    brokers = "192.168.1.100:9092" 
    # brokers = "43.198.68.123:9092"
    producer = confluent_kafka.Producer({'bootstrap.servers': brokers})
    consumer = confluent_kafka.Consumer({'bootstrap.servers': brokers, 'group.id': 'mygroup'})
    topics = consumer.list_topics()
    print("Available topics:", topics.topics.keys())
    assert producer is not None
    assert consumer is not None
    return True

if __name__ == '__main__':
    f = test_connections()
    print(f)
