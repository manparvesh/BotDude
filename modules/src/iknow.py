import random
from templates.text import TextTemplate


def process(input):
    iknow = [
        'I know everything dude! Just too lazy to type all that!'
    ]
    output = {
        'input': input,
        'output': TextTemplate(random.choice(iknow)).get_message(),
        'success': True
    }
    return output
