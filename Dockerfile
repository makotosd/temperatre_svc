#
#
#
FROM ubuntu
RUN apt-get update -q -y && \
    apt-get upgrade -y && \
    apt-get install -y python-pip curl && \
    pip install wiringpi flask
COPY temperature_svc.py /

EXPOSE 8080

ENTRYPOINT ["python", "/temperature_svc.py"]
