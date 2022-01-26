# rasa-wiki-spirit
A [RASA](https://rasa.com/) bot with the support of wikipedia API.
(rasa version = 3.0)


# Usage

## Train the RASA conversation model
- cd chatbot
- rasa train

## localhost chatbot service
1. Start a rasa action server
  - cd chatbot
  - rasa run actions

2. Start a rasa chatbot server in another terminal
  - cd chatbot
  - `rasa run --enable-api --cors "*" --debug`

3. Start a web service with [webchat widget](https://github.com/botfront/rasa-webchat)
  - cd webchat
  - python app.py

