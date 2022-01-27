FROM python:3.8-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .
COPY templates/index_docker.html templates/index.html


CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
# CMD [ "python3", "app.py"]
