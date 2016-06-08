import requests
from templates.text import TextTemplate
from random import choice
import json
import config


def process(input):
    output = {}
    try:
        with open(config.JOKES_SOURCE_FILE) as jokes_file:
            jokes = json.load(jokes_file)
            jokes_list = jokes['jokes']
            output['input'] = input
            output['output'] = TextTemplate(choice(jokes_list)).get_message()
            output['success'] = True
    except:
        output['success'] = False
    return output
