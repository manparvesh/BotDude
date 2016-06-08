import random
from templates.text import TextTemplate


def process(input):
    bye = [
        'Bye dude!',
        'Goodbye, dude!',
        'See ya later, dude!',
        'Peace out, dude!',
        'Later, dude!'
    ]
    output = {
        'input': input,
        'output': TextTemplate(random.choice(bye)).get_message(),
        'success': True
    }
    return output
