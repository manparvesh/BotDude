import random
from templates.text import TextTemplate


def process(input):
    emoji = [
        ':P',
        'B|',
        '-_-',
        ':D'
    ]
    output = {
        'input': input,
        'output': TextTemplate(random.choice(emoji)).get_message(),
        'success': True
    }
    return output
