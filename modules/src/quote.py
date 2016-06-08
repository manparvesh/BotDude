import requests
from templates.text import TextTemplate
from random import choice
import json
import config


def process(input):
    output = {}
    try:
        with open(config.QUOTES_SOURCE_FILE) as quotes_file:
            quotes = json.load(quotes_file)
            quotes_list = quotes['quotes']
            output['input'] = input
            output['output'] = TextTemplate(choice(quotes_list)).get_message()
            output['success'] = True
    except:
        output['success'] = False
    return output
