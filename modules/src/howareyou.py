import random
from templates.text import TextTemplate


def process(input):
    howareyou = [
        'I\'m amazing, dude!',
        'I\'m awesome, dude!'
    ]
    output = {
        'input': input,
        'output': TextTemplate(random.choice(howareyou)).get_message(),
        'success': True
    }
    return output
