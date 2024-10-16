import confluent_kafka

def test_connections():
    brokers = "localhost:9091"
    producer = confluent_kafka.Producer({'bootstrap.servers': brokers})
    consumer = confluent_kafka.Consumer({'bootstrap.servers': brokers, 'group.id': 'mygroup'})
    assert producer is not None
    assert consumer is not None
    return True

if __name__ == '__main__':
    f = test_connections()
    print(f)