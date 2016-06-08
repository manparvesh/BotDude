import random
from templates.text import TextTemplate


def process(input):
    cuss = [
        'Damn! You need language lessons, dude!',
        'Easy there, dude!',
        'Dude! Tongue!',
        'Control, dude!'
    ]
    output = {
        'input': input,
        'output': TextTemplate(random.choice(cuss)).get_message(),
        'success': True
    }
    return output
