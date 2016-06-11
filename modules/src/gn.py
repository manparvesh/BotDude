import random
from templates.text import TextTemplate


def process(input):
    gn = [
        'Night, dude!',
        'Good night, dude! Sleep tight! :P'
    ]
    output = {
        'input': input,
        'output': TextTemplate(random.choice(gn)).get_message(),
        'success': True
    }
    return output
