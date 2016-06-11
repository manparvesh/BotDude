import random
from templates.text import TextTemplate


def process(input):
    ge = [
        'Evening, dude!',
        'Good evening, dude!'
    ]
    output = {
        'input': input,
        'output': TextTemplate(random.choice(ge)).get_message(),
        'success': True
    }
    return output
