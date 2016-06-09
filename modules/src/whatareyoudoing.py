import random
from templates.text import TextTemplate


def process(input):
    whatareyoudoing = [
        'I\'m talking to you while having a White Russian cocktail, dude!',
        'Chillin\'!'
    ]
    output = {
        'input': input,
        'output': TextTemplate(random.choice(whatareyoudoing)).get_message(),
        'success': True
    }
    return output
