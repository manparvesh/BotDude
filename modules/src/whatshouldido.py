import random
from templates.text import TextTemplate


def process(input):
    whatshouldido = [
        'You should learn to chill, dude!',
        'Have a White Russian cocktail, dude!',
        'Relax, dude!',
        'Have fun, dude!'
    ]
    output = {
        'input': input,
        'output': TextTemplate(random.choice(whatshouldido)).get_message(),
        'success': True
    }
    return output
