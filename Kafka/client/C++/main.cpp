#include <iostream>
#include <string>
#include <librdkafka/rdkafkacpp.h>

int main() {
  std::string brokers = "localhost:9092";
  std::string errstr;
  RdKafka::Conf *conf = RdKafka::Conf::create(RdKafka::Conf::CONF_GLOBAL);
  conf->set("metadata.broker.list", brokers, errstr);

  RdKafka::Producer *producer = RdKafka::Producer::create(conf, errstr);
  if (!producer) {
    std::cerr << "Failed to create producer: " << errstr << std::endl;
    return 1;
  }

  RdKafka::Topic *topic = RdKafka::Topic::create(producer, "test", NULL, errstr);
  if (!topic) {
    std::cerr << "Failed to create topic: " << errstr << std::endl;
    return 1;
  }

  std::string value = "Hello, Kafka!";
  RdKafka::ErrorCode resp = producer->produce(topic, RdKafka::Topic::PARTITION_UA,
                                              RdKafka::Producer::RK_MSG_COPY,
                                              const_cast<char *>(value.c_str()), value.size(),
                                              NULL, NULL);
  if (resp != RdKafka::ERR_NO_ERROR) {
    std::cerr << "Failed to produce: " << RdKafka::err2str(resp) << std::endl;
    return 1;
  }

  producer->poll(0);
  producer->flush(1000);

  delete topic;
  delete producer;
  delete conf;

  return 0;
}
 
//  The code is pretty straightforward. It creates a producer, a topic, and sends a message to the topic. 
//  To compile the code, you need to link against the librdkafka library. 
//  $ g++ -o producer producer.cpp -lrdkafka++
 
//  To run the producer, you need to have a Kafka broker running on localhost:9092. 
//  $ ./producer
 
//  If everything goes well, you should see the message "Hello, Kafka!" in the topic "test". 
//  Consuming messages 
//  Now let's write a consumer that reads messages from the topic "test".