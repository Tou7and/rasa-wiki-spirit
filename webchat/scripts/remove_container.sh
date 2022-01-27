#!/bin/bash

NAME="flask_webchat"

echo "Stopping Flask webchat ..."

docker stop $NAME
docker rm $NAME

