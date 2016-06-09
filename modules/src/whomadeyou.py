import random
from templates.text import TextTemplate


def process(input):
    whomadeyou = [
        'An awesome dude, dude!',
        'A super cool dude, dude!',
        'Batman! Nananana!'
    ]
    output = {
        'input': input,
        'output': TextTemplate(random.choice(whomadeyou)).get_message(),
        'success': True
    }
    return output
