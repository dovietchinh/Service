# KAFKA SETUP 

history of kafka [story](https://double.cloud/blog/posts/2023/04/confluent-kafka-vs-apache-kafka/)

## Comparision

Apache Kafka:

    - Early
    - Open-source
    - Easy to use
    - 

Confluent Kafka:

    - More feaature for enterprice
    - Schema Registry.
    - Another is ksqlDB

## Role of Zookeeper

- Metadata management: bao gồm vị trí các broker, cấu hình topic, và các partition.
    
- Leadership voting: Bầu leader cho mỗi partition của 1 topics.Điều này đảm bảo rằng chỉ có 1 broker  chịu trách nhiệm xử lý cho 1 phân vùng.
cụ thể vào bất kì thời điểm nào.

- Quản lý consumer trong group offsets: Zookeeper được sử dụng để lưu vị trí đọc hiện tại (current offset) của mỗi  consumer group.
Cho phép consumer tiếp tục đọc tiếp từ vị trí cũ khi lỗi hay khởi động lại.

- Health check. Giám sát sức khỏe của cụm kafka và có thể thông báo cho quản trị viên nếu có bất kỳ vấn đề nào phát sinh.


### Mode Kraft là gì?

Config để không cần dùng Zookeeper, nếu sử dụng Zookeeper tốt rồi thì k cần 
