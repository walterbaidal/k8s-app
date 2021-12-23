FROM ubuntu:18.04

RUN apt-get update -y && \
    apt install -y software-properties-common

RUN add-apt-repository -y ppa:deadsnakes/ppa

RUN apt install -y python3.9

RUN apt-get -y install python3-pip
# RUN ln -sf /usr/bin/python3.9 /usr/bin/python3

WORKDIR /app

COPY . /app

RUN python3 setup.py develop

WORKDIR /app/src

ENTRYPOINT [ "python3" ]

EXPOSE 5000:5000

CMD [ "app.py" ]
