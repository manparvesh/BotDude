import random
from templates.text import TextTemplate


def process(input):
    changethis = [
        'Too lazy for that, dude!',
        'Relax, dude! Don\'t interfere with my laziness!'
    ]
    output = {
        'input': input,
        'output': TextTemplate(random.choice(changethis)).get_message(),
        'success': True
    }
    return output
