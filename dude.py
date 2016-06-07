from flask import Flask, request
import requests
import re
import random

app = Flask(__name__)

ACCESS_TOKEN = "EAALGzZACE8t0BABrOY4kklZBTBZBo3wZAsX8GFcN588ZAp87"
ACCESS_TOKEN += "j7tBRPGYzGxbxLvSk4tAZBe4o"
ACCESS_TOKEN += "Pyr0FZBAE8x88xZByGsRRGZAl2uT24vWzTubLf7AxfjYZCG4yUiTody"
ACCESS_TOKEN += "1HS0PqSxHDWqu34NLngWyyTBKmfDQlnCzkySGAVGkr0DftNAZDZD"
VERIFY_TOKEN = "abcd"


def sayHi(received_message):
    hello = {'hi': "Hi dude!", 'hello': "Hi dude!"}

    tokens = re.sub(r"[^a-zA-Z0-9\s]", ' ', received_message).lower().split()
    for token in tokens:
        if token in hello:
            return jokes[token]
    return "You don't make sense to me dude!"

# you know, that's just, your opinion dude!


def reply(user_id, msg):
    data = {
        "recipient": {"id": user_id},
        "message": {"text": sayHi(msg)}
    }
    url = "https://graph.facebook.com/v2.6/me/messages?access_token="
    resp = requests.post(url + ACCESS_TOKEN, json=data)
    print(resp.content)


@app.route('/', methods=['GET'])
def handle_verification():
    if request.args['hub.verify_token'] == VERIFY_TOKEN:
        return request.args['hub.challenge']
    else:
        return "Invalid verification token"


@app.route('/', methods=['POST'])
def handle_incoming_messages():
    data = request.json
    sender = data['entry'][0]['messaging'][0]['sender']['id']
    message = data['entry'][0]['messaging'][0]['message']['text']
    reply(sender, message)

    return "ok"


if __name__ == '__main__':
    app.run(debug=True)
