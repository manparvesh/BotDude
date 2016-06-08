import config
from flask import Flask, request
import requests
import re
import random
import os
import modules


app = Flask(__name__)

ACCESS_TOKEN = os.environ.get('ACCESS_TOKEN', config.ACCESS_TOKEN)
VERIFY_TOKEN = os.environ.get('VERIFY_TOKEN', config.VERIFY_TOKEN)


def processReply(msg):
    return modules.search(msg)


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
        sender = event['sender']['id']
        message = event['message']['text']

        reply(sender, message)

        return "ok"
    return "not ok"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)), debug=True)
