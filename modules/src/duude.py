import random
from templates.text import TextTemplate


def process(input):
    duude = [
        'Duuuuude! Relax!',
        'You need a White Russian cocktail! So do I',
        'Damn dude!',
        'Daaaaaammmmnnnnn!'
    ]
    output = {
        'input': input,
        'output': TextTemplate(random.choice(duude)).get_message(),
        'success': True
    }
    return output
