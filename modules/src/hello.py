import random
from templates.text import TextTemplate


def process(input):
    hello = [
        'Hi dude!',
        'Hey there, dude!',
        'Yo dude!',
        'What\'s up, dude!'
    ]
    output = {
        'input': input,
        'output': TextTemplate(random.choice(hello)).get_message(),
        'success': True
    }
    return output
