docker run \
  --name=filebeat \
  --user=root \
  --volume=${PWD}/filebeat.yml:/usr/share/filebeat/filebeat.yml:ro \
  --net=elk_network \
  docker.elastic.co/beats/filebeat:8.14.0 filebeat -e