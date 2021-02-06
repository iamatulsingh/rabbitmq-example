FROM ubuntu:18.04

RUN apt-get update -y && \
    apt-get install -y python3-pip python3-dev

COPY ./req.txt /app/req.txt

WORKDIR /app

RUN pip3 install -r req.txt

COPY . /app

ENTRYPOINT [ "python3" ]

CMD [ "app.py" ]

