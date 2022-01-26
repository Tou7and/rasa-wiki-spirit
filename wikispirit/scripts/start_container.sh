#!/bin/bash

DOCKER_TAG="tou7and/rasa-sdk:3.0.2-wikispirit"

NAME="rasa_wikispirit"

echo "Starting RASA wikispirit ..."

docker run -d \
    --restart unless-stopped \
    -p 5000:5000 \
    --name $NAME $DOCKER_TAG

