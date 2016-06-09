import random
from templates.text import TextTemplate


def process(input):
    talktome = [
        'I am talking to you, dude!',
        'Dude!'
    ]
    output = {
        'input': input,
        'output': TextTemplate(random.choice(talktome)).get_message(),
        'success': True
    }
    return output
