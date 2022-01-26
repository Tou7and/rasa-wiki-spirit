FROM python:3.8-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

RUN python3 -m spacy download zh_core_web_md

RUN pip3 install sanic==21.6.0
RUN pip3 install sanic-jwt==1.7.0
RUN pip3 install sanic-plugin-toolkit==1.2.1
RUN pip3 install sanic-routing==0.7.0
RUN pip3 install gevent-websocket==0.10.1
RUN pip3 install eventlet==0.33.0

COPY ./actions /app/actions
COPY ./data /app/data
COPY ./models /app/models

COPY ./domain.yml /app/
COPY ./config.yml /app/
COPY ./credentials.yml /app/
COPY ./backup/endpoints.yml /app/

