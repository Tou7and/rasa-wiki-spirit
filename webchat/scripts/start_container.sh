#!/bin/bash

DOCKER_TAG="tou7and/flask:rasa-webchat"
NAME="flask_webchat"

echo "Starting Flask webchat ..."

docker run -d \
    --restart unless-stopped \
    -p 5000:5000 \
    --name $NAME $DOCKER_TAG

