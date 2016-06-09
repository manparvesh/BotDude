import random
from templates.text import TextTemplate


def process(input):
    frustration = [
        'Easy there, dude!',
        'Control dude!',
        'You need to chill, dude!'
    ]
    output = {
        'input': input,
        'output': TextTemplate(random.choice(frustration)).get_message(),
        'success': True
    }
    return output
