from flask import Flask, request
import requests
import re
import random
import os

app = Flask(__name__)

ACCESS_TOKEN = "EAALGzZACE8t0BABrOY4kklZBTBZBo3wZAsX8GFcN588ZAp87"
ACCESS_TOKEN += "j7tBRPGYzGxbxLvSk4tAZBe4o"
ACCESS_TOKEN += "Pyr0FZBAE8x88xZByGsRRGZAl2uT24vWzTubLf7AxfjYZCG4yUiTody"
ACCESS_TOKEN += "1HS0PqSxHDWqu34NLngWyyTBKmfDQlnCzkySGAVGkr0DftNAZDZD"
VERIFY_TOKEN = "abcd"


hello = {'hi': "Hi dude!", 'hello': "Hi dude!"}


def sayHi(token):
    return hello[token]

# you know, that's just, your opinion dude!


def sayBye():
    return "Goodbye, Dude!"


def intro():
    return "I'm the dude, dude!"


def processReply(msg):
    tokens = re.sub(r"[^a-zA-Z0-9\s]", ' ', msg).lower().split()

    if "who" in token:
        return intro()

    for token in tokens:
        if token in hello:
            return sayHi(token)
        elif token == "bye" or "goodbye":
            return sayBye()
    return "You don't make sense to me dude!"


def reply(user_id, msg):
    data = {
        "recipient": {"id": user_id},
        "message": {"text": processReply(msg)}
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
    event = data['entry'][0]['messaging'][0]
    if 'message' in event and 'text' in event['message']:
        sender = data['entry'][0]['messaging'][0]['sender']['id']
        message = data['entry'][0]['messaging'][0]['message']['text']

        reply(sender, message)

        return "ok"
    return "not ok"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)), debug=True)
