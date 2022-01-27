# rasa-wiki-spirit
A [RASA](https://rasa.com/) bot with the support of wikipedia API.
(rasa version = 3.0)


# Usage

## Train the RASA conversation model
- cd chatbot
- rasa train

## localhost chatbot service
1. Start a rasa action server
    - cd wikispirit
    - rasa run actions

2. Start a rasa chatbot server in another terminal
    - cd wikispirit
    - `rasa run --enable-api --cors "*" --debug`

3. Start a web service with [webchat widget](https://github.com/botfront/rasa-webchat)
    - cd webchat
    - python app.py

## deploy via docker-compose
1. Build image
    - cd wikispirit
    - `scripts/build_image.sh`

2. Docker compose
    - cd wikispirit
    - docker-compose up -d

3. Start a web service with [webchat widget](https://github.com/botfront/rasa-webchat)
    - cd webchat
    - python app.py

