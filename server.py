from flask import Flask, request
import requests, re, random

app = Flask(__name__)

ACCESS_TOKEN = "EAALGzZACE8t0BABrOY4kklZBTBZBo3wZAsX8GFcN588ZAp87j7tBRPGYzGxbxLvSk4tAZBe4oPyr0FZBAE8x88xZByGsRRGZAl2uT24vWzTubLf7AxfjYZCG4yUiTody1HS0PqSxHDWqu34NLngWyyTBKmfDQlnCzkySGAVGkr0DftNAZDZD"
VERIFY_TOKEN = "abcd"

def processReply(received_message):
	jokes = { 'stupid': ["""Yo' Mama is so stupid, she needs a recipe to make ice cubes.""",  """Yo' Mama is so stupid, she thinks DNA is the National Dyslexics Association."""], 
        'fat':      ["""Yo' Mama is so fat, when she goes to a restaurant, instead of a menu, she gets an estimate.""", """ Yo' Mama is so fat, when the cops see her on a street corner, they yell, "Hey you guys, break it up!" """], 
        'dumb': ["""Yo' Mama is so dumb, when God was giving out brains, she thought they were milkshakes and asked for extra thick.""",  """Yo' Mama is so dumb, she locked her keys inside her motorcycle."""] }
        
	tokens = re.sub(r"[^a-zA-Z0-9\s]",' ',recevied_message).lower().split()
	for token in tokens:
		if token in jokes:
			return random.choice(jokes[token])
	return "I didn't understand! Send 'stupid', 'fat', 'dumb' for a Yo Mama joke!"         


def reply(user_id, msg):
    data = {
        "recipient": {"id": user_id},
        "message": {"text": msg}
    }
    resp = requests.post("https://graph.facebook.com/v2.6/me/messages?access_token=" + ACCESS_TOKEN, json=data)
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
    reply(sender, processReply(message))

    return "ok"


if __name__ == '__main__':
    app.run(debug=True)
