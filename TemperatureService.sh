#docker run -d --rm --privileged -p 8080:8080 --network sensor-network --name sensor tmc05/temperature_svc
docker run -d --rm --privileged --network sensor-network --name sensor tmc05/temperature_svc
