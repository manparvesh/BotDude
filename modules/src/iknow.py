import random
from templates.text import TextTemplate


def process(input):
    iknow = [
        'I know everything dude!',
        'I\'m amazing, dude! You don\'t know me yet.',
        'I\'m batman'
    ]
    output = {
        'input': input,
        'output': TextTemplate(random.choice(iknow)).get_message(),
        'success': True
    }
    return output
