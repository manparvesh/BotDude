import random
from templates.text import TextTemplate


def process(input):
    gm = [
        'Morning, dude!',
        'Good morning, dude!'
    ]
    output = {
        'input': input,
        'output': TextTemplate(random.choice(gm)).get_message(),
        'success': True
    }
    return output
