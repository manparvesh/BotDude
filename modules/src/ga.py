import random
from templates.text import TextTemplate


def process(input):
    ga = [
        'Afternoon, dude!',
        'Good afternoon, dude!'
    ]
    output = {
        'input': input,
        'output': TextTemplate(random.choice(ga)).get_message(),
        'success': True
    }
    return output
