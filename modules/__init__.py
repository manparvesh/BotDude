import config
import os
import requests
import sys
from src import *
from templates.text import TextTemplate

API_AI_TOKEN = os.environ.get('WIT_AI_ACCESS_TOKEN', config.API_AI_TOKEN)
excuse = 'Didn\'t work! I need a White Russian cocktail to relax, dude.'
typeHelp = 'I don\'t get you, dude.\nTry typing "help".'


def process_query(input):
    try:
        url = 'https://api.api.ai/api/query?v=20150910&query=' + input
        url += '&lang=en&sessionId=883b4790-0f67-46ac-9'
        url += '18e-5b5e3fa54137&timezone=Asia/Calcutta'
        r = requests.get(url, headers={
            'Authorization': 'Bearer %s' % API_AI_TOKEN
        })
        data = r.json()
        intent = data['result']['metadata']['intentName']
        if intent in src.__all__:
            return intent
        else:
            return None
    except:
        return None


def search(input):
    intent = process_query(input)
    if intent is not None:
        data = sys.modules['modules.src.' + intent].process(input)
        if data['success']:
            return data['output']
        else:
            if 'error_msg' in data:
                return data['error_msg']
            else:
                return TextTemplate(excuse).get_message()
    else:
        return TextTemplate(typeHelp).get_message()
